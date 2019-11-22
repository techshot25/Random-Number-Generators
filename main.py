from matplotlib import pyplot as plt

from math import log

def lcg(seed=4321, m=7829, a=378, c=2310):
    running_val = seed
    nums = set()
    while running_val not in nums:
        nums.add(running_val)
        running_val = (running_val * a + c) % m
    nums = list(nums)
    return [num/max(nums) for num in nums]

inverse_cdf = lambda x: -log(1 / x - 1) if (1 > x > 0) else 0

x = lcg(4232)
y = [inverse_cdf(val) for val in x]

plt.hist(y, bins=20)
plt.show()
