
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

mu = 0.5
sigma = np.sqrt(1/12)
m = 1000
n_values = [2, 5, 10, 30, 50]

output_dir = "../results/figures"
os.makedirs(output_dir, exist_ok=True)

np.random.seed(42)

for n in n_values:
    sums = np.sum(np.random.uniform(0, 1, (m, n)), axis=1)
    z = (sums - n * mu) / (sigma * np.sqrt(n))

    plt.figure(figsize=(8, 5))
    plt.hist(z, bins=30, density=True, alpha=0.6)
    x = np.linspace(-4, 4, 200)
    plt.plot(x, stats.norm.pdf(x), linewidth=2)
    plt.title(f"CLT Histogram (n = {n})")
    plt.xlabel("Z")
    plt.ylabel("Density")
    plt.grid(True)
    plt.savefig(f"{output_dir}/clt_histogram_n{n}.png", dpi=300)
    plt.close()

    plt.figure(figsize=(5, 5))
    stats.probplot(z, dist="norm", plot=plt)
    plt.title(f"Q-Q Plot (n = {n})")
    plt.grid(True)
    plt.savefig(f"{output_dir}/clt_qqplot_n{n}.png", dpi=300)
    plt.close()
