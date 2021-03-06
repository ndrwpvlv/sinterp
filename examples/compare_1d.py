import random
import time

from numpy import interp

from sinterp import interp1d

times = []  # list with time of calculation
ratios = []  # ratio of calc with interp to interp1d
deltas = []  # summary delta of difference results by iteration
size = []

for kk in range(2, 5):
    x1 = 0
    x2 = int(10 ** kk)
    size.append(x2)

    xp = [float(_) for _ in range(x1, x2 + 1)]
    yp = [_ ** 3.0 for _ in xp]

    x = [random.uniform(float(x1), float(x2)) for _ in range(10000)]

    start_time = time.time()
    v_1 = [interp(_, xp, yp) for _ in x]
    time_1 = time.time() - start_time

    start_time = time.time()
    v_2 = [interp1d(_, xp, yp) for _ in x]
    time_2 = time.time() - start_time

    times.append([time_1, time_2])
    ratios.append(time_1 / time_2)
    deltas.append(sum(_[1] - _[0] for _ in zip(v_1, v_2)))

# Print benchmark ratios
print('--- Benchmark results ---')
print('List size : Ratio')
for r, v in zip(size, ratios):
    print('    %i : %f' % (r, v))
print('Check convergence. Difference between interp and interp1d = %f' % max(deltas))
