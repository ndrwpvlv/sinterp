# sinterp
Simple fast linear interpolation for Python

Simple benchmark for compare with Numpy:
```python
from numpy import interp
import random
import time

from sinterp.sinterp import interp1d

times = []  # list with time of calculation
ratios = []  # ratio of calc with interp to interp1d
deltas = []  # summary delta of difference results by iteration
size = []

for kk in range(1, 6):
    x1 = 0
    x2 = int(10 ** kk)
    size.append(x2)

    xp = [float(_) for _ in range(x1, x2 + 1)]
    yp = [_**3.0 for _ in xp]

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
```
Results Python 3.6 Win10 (at my laptop):
```
--- Benchmark results ---
List size : Ratio
    10 : 2.312361
    100 : 1.810310
    1000 : 7.835562
    10000 : 54.542985
    100000 : 514.559448
Check convergence. Delta between interp and interp1d = 0.000000
```
Results Python 3.7 Linux-Mint 19.3
```
--- Benchmark results ---
List size : Ratio
    10 : 2.409009
    100 : 3.836711
    1000 : 19.986599
    10000 : 141.633523
    100000 : 1155.362543
Check convergence. Delta between interp and interp1d = 0.000000
```