#
# (C) 2014-2017 Seiji Matsuoka
# Licensed under the MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import unittest

from tornado.testing import AsyncTestCase, gen_test

from flashflood.core.container import Container
from flashflood.core.task import Task
from flashflood.core.workflow import Workflow
from flashflood.node.reader.iterinput import IterInput
from flashflood.node.transform.stack import Stack
from flashflood.node.writer.container import ContainerWriter


RECORDS = [
    {"id": 1, "type": "a", "value": 12.4},
    {"id": 2, "type": "b", "value": 54.23},
    {"id": 3, "type": "c", "value": 111},
    {"id": 4, "type": "a", "value": 98.0},
    {"id": 5, "type": "c", "value": None}
]


class TestStack(AsyncTestCase):
    @gen_test
    def test_stack(self):
        wf = Workflow()
        wf.interval = 0.01
        result = Container()
        wf.append(IterInput(RECORDS))
        wf.append(Stack(('id',)))
        wf.append(ContainerWriter(result))
        task = Task(wf)
        yield task.execute()
        self.assertEqual(len(list(result.records)), 9)

    @gen_test
    def test_skip_none(self):
        wf = Workflow()
        wf.interval = 0.01
        result = Container()
        wf.append(IterInput(RECORDS))
        wf.append(Stack(('id',), skip_none=False))
        wf.append(ContainerWriter(result))
        task = Task(wf)
        yield task.execute()
        self.assertEqual(len(list(result.records)), 10)


if __name__ == '__main__':
    unittest.main()
