import random
import time

from numpy import meshgrid, array
from scipy.interpolate import interp2d as sc_interp2d

from sinterp import interp2d as si_interp2d

times = []  # list with time of calculation
ratios = []  # ratio of calc with interp to interp1d
deltas = []  # summary delta of difference results by iteration
size = []

for kk in range(2, 5):
    x1 = 0
    x2 = int(10 ** kk)
    size.append(x2)
    xp = [float(_) for _ in range(0, x2 + 1)]
    yp = [float(_) for _ in range(0, x2 + 1)]
    zp = [[x * y for y in yp] for x in xp]

    XP_GRID, YP_GRID = meshgrid(xp, yp)
    ZP_GRID = array(zp)

    xv = [random.uniform(0.0, x2) for _ in range(1000)]
    yv = [random.uniform(0.0, x2) for _ in range(1000)]

    start_time = time.time()
    sci_interp2d = sc_interp2d(xp, yp, zp)
    v_1 = [sci_interp2d(x, y) for x, y in zip(xv, yv)]
    time_1 = time.time() - start_time

    start_time = time.time()
    v_2 = [si_interp2d(x, y, xp, yp, zp) for x, y in zip(xv, yv)]
    time_2 = time.time() - start_time

    times.append([time_1, time_2])
    ratios.append(time_1 / time_2)
    deltas.append(sum(_[1] - _[0] for _ in zip(v_1, v_2)))

# Print benchmark ratios
print('--- Benchmark results ---')
print('List size : Ratio')
for r, v in zip(size, ratios):
    print('    %i : %f' % (r, v))
print('Check convergence. Difference between interp2d (scipy) and interp2d (sinterp) = %f' % max(deltas))
