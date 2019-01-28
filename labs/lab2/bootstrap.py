import random

import matplotlib
from pandas.core.resample import resample
from scipy.stats import stats

matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np



def boostrap(sample, sample_size, iterations):
    # <---INSERT YOUR CODE HERE--->
    means = []
    data_mean = np.mean(sample)
    for iteration in range(iterations):
        new_sample = resample(sample, sample_size= 21)
        means.append(np.mean(new_sample))

    bounds  = [0,0]
    bounds[0] = np.percentile(means, 5)
    bounds [1] = np.percentile(means, 95)
    lower = bounds[0]
    upper = bounds[1]


    print(data_mean , "/" , lower ,"/", upper )
    return data_mean, lower, upper


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')

    data = df.values.T[0]
    boots = []
    for i in range(100, 100000, 1000):
        boot = boostrap(data, data.shape[0], i)
        boots.append([i, boot[0], "mean"])
        boots.append([i, boot[1], "lower"])
        boots.append([i, boot[2], "upper"])

    df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
    sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, 100000)

    sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
    sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')

# print ("Mean: %f")%(np.mean(data))
# print ("Var: %f")%(np.var(data))
