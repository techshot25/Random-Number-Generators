# %% generate a random normal distribution

from matplotlib import pyplot as plt
from math import log, erf

def lcg(seed=4321, m=7829, a=378, c=2310):
    running_val = seed
    nums = set()
    while running_val not in nums:
        nums.add(running_val)
        running_val = (running_val * a + c) % m
        yield running_val / (m - 1)

uniform_random_samples = [num for num in lcg()]
plt.hist(uniform_random_samples, bins=50)
plt.show()

# %%

def generate(inverse_cdf=None, seed=4321, m=7829, a=378, c=2310):
    running_val = seed
    nums = set()
    while running_val not in nums:
        nums.add(running_val)
        running_val = (running_val * a + c) % m
        if callable(inverse_cdf):
            yield inverse_cdf(running_val / (m - 1))
        else:
            yield running_val / (m - 1)

normal = lambda x: -log(1 / x - 1) if (1 > x > 0) else 0

li = [val for val in generate(inverse_cdf=normal)]
plt.hist(li, bins=50)
plt.show()

# %%

exponential = lambda x: -log(x) if (1 > x > 0) else 0

li = [val for val in generate(inverse_cdf=exponential)]
plt.hist(li, bins=50)
plt.show()


# %%
