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


import sys
import multired as mr

if len(sys.argv) < 2:
    print("Usage: %s <layer_list>" % sys.argv[0])
    sys.exit(1)

print("Loading layers...")
m = mr.multiplex_red(sys.argv[1], verbose=True)
print("[DONE]")

print("Computing layer entropies...")
m.compute_layer_entropies()
print("[DONE]")

print("Computing JSD matrix...")
m.compute_JSD_matrix()
print("[DONE]")

print("Performing reduction...")
m.reduce()
print("[DONE]")

print("Getting partitons...")
part = m.compute_partitions()
print("[DONE]")

print("Partitions:...")
m.dump_partitions()
print("[DONE]")

m.draw_dendrogram(saveas='dendrogram.png')
