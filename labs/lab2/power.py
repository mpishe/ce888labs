import random

import numpy as np
from scipy.stats import stats


def resample(sample, sample_size):
    new_sample = []
    for i in range(sample_size):
        new_sample.append(random.choice(sample))
    return new_sample
def returnPower(new_sample1, new_sample2, size):
    # Calculate the variance to get the standard deviation
    var_a = np.var(new_sample1, ddof=1)
    var_b = np.var(new_sample2, ddof=2)
    # std deviation
    s = np.sqrt((var_a + var_b) / 2)
    ## Calculate the t-statistics
    t = (np.mean(new_sample1) - np.mean(new_sample2)) / (s * np.sqrt(2 / size))
    ## Compare with the critical t-value
    # Degrees of freedom
    df = 2 * size - 2
    # p-value after comparison with the t
    p = 1 - stats.t.cdf(t, df=df)
    return p
def power(sample1, sample2, reps, size, alpha):
    count  = 0
    for i  in range(reps):
        new_sample1 = resample(sample1, size)
        new_sample2 = resample(sample2, size)
        if(returnPower(new_sample1, new_sample2, size) < 1-alpha):
            count += 1
    return (count* 100) /reps

