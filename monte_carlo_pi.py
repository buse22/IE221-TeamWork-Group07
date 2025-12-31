
import numpy as np
import matplotlib.pyplot as plt
import os
import math

n = 10000
np.random.seed(42)

x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

inside = x**2 + y**2 <= 1
pi_estimates = 4 * np.cumsum(inside) / np.arange(1, n + 1)

plt.figure(figsize=(10, 6))
plt.plot(pi_estimates, label="Monte Carlo π Estimate")
plt.axhline(y=math.pi, linestyle="--", label="True π")
plt.xlabel("Number of Points (n)")
plt.ylabel("π Estimate")
plt.title("Monte Carlo Estimation of π")
plt.legend()
plt.grid(True)

output_dir = "../results/figures"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f"{output_dir}/pi_estimation.png", dpi=300)
plt.show()
