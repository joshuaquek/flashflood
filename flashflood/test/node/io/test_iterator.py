#
# (C) 2014-2017 Seiji Matsuoka
# Licensed under the MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import unittest

from tornado.testing import AsyncTestCase

from flashflood.node.io.iterator import IteratorInput


class TestIteratorInput(AsyncTestCase):
    def test_iterator_input(self):
        f = IteratorInput(range(100))
        f.on_submitted()
        self.assertEqual(f.out_edge(0).task_count, 100)
        f.run()
        self.assertEqual(sum(f.out_edge(0).records), 4950)


if __name__ == '__main__':
    unittest.main()