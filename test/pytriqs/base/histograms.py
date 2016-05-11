from pytriqs.statistics import *
from pytriqs.utility.comparison_tests import *
import numpy as np

hi1 = Histogram(0, 10)
data = [-1, 0, 0, 0, 1, 2, 2, 2, 3, 5, 9, 32]
for i in data: hi1 << i

hd1 = Histogram(0, 10, 21)
data = [-10, -0.05, 1.1, 2.0, 2.2, 2.9, 3.4, 5, 9, 10.0, 10.5, 12.1, 32.2]
for i in data: hd1 << i

hi2 = Histogram(0, 10)
data = [1.1, 2.0, 2.2, 2.9, 3.4, 5, 9, 10.0, 10.1, 12.1, 32.2]
for i in data: hi2 << i

hd2 = Histogram(0, 10, 11)
data = [1.1, 2.0, 2.2, 2.9, 3.4, 5, 9, 10.0, 10.1, 12.1, 32.2]
for i in data: hd2 << i

hd3 = Histogram(0, 10, 11)
hd3 << 1.1 << 2.0 << 2.2 << 2.9 << 3.4 << 5 << 9 << 10.0 << 10.1 << 12.1 << 32.2
    
true_hi1 = np.array([3, 1, 3, 1, 0, 1, 0, 0, 0, 1, 0])
true_hd1 = np.array([0, 0, 1, 0, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
true_h2 = np.array([0, 1, 2, 2, 0, 1, 0, 0, 0, 1, 1])

assert_arrays_are_close(hi1.data, true_hi1)
assert(hi1.n_lost_pts == 2)
assert(hi1.n_data_pts == 10)

cdf_hi1 = cdf(hi1)
assert(cdf_hi1.data[cdf_hi1.size - 1] == 1.0)

assert_arrays_are_close(hd1.data, true_hd1)
assert(hd1.n_lost_pts == 5)

assert_arrays_are_close(hi2.data, true_h2)
assert(hi2.n_lost_pts == 3)
assert_arrays_are_close(hi2.data, hd2.data)
assert_arrays_are_close(hd2.data, hd3.data)
