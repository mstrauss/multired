#
#
#  test.py
#
#
#  Copyright (C) 2015 Vincenzo (Enzo) Nicosia <katolaz@yahoo.it>
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  long with this program.  If not, see  <http://www.gnu.org/licenses/>.
#

from unittest import TestCase

import multired as mr


class TestMultired(TestCase):

    sample_filelist = 'sample_data/file_list'

    def test(self):
        m = mr.multiplex_red(self.sample_filelist)
        m.compute_layer_entropies()
        m.compute_JSD_matrix()
        m.reduce()
        m.compute_partitions()
        m.dump_partitions()
        m.draw_dendrogram()

    def test_simple(self):
        m = mr.multiplex_red(self.sample_filelist)
        part = m.compute_partitions()
        assert part == [(0.15661326155470412, [[0], [1], [2], [3]]),
                        (0.17899837524783313, [[1], [2], [0, 3]]),
                        (0.2394715269325508, [[1], [2, 0, 3]]),
                        (0.0, [[1, 2, 0, 3]])]
        m.dump_partitions()

    def test_approx(self):
        m = mr.multiplex_red(self.sample_filelist)
        m.compute_layer_entropies_approx()
        m.compute_JSD_matrix_approx()
        m.reduce_approx()
        m.compute_partitions_approx()
        m.dump_partitions_approx()
        m.draw_dendrogram_approx()

    def test_approx_simple(self):
        m = mr.multiplex_red(self.sample_filelist)
        part = m.compute_partitions_approx()
        assert part == [(0.12253003685170516, [[0], [1], [2], [3]]),
                        (0.14136825670745423, [[1], [2], [0, 3]]),
                        (0.19553392690309745, [[1], [2, 0, 3]]),
                        (0.0, [[1, 2, 0, 3]])]
        m.dump_partitions_approx()
