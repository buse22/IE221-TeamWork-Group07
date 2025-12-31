
import numpy as np
import matplotlib.pyplot as plt
import os

n = 10000
mu = 0.5

np.random.seed(42)
samples = np.random.uniform(0, 1, n)
cumulative_mean = np.cumsum(samples) / np.arange(1, n + 1)

plt.figure(figsize=(10, 6))
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.axhline(y=mu, linestyle="--", label="True Mean (μ = 0.5)")
plt.xlabel("Number of Observations (n)")
plt.ylabel("Cumulative Mean")
plt.title("SLLN Simulation")
plt.legend()
plt.grid(True)

output_dir = "../results/figures"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f"{output_dir}/slln_convergence.png", dpi=300)
plt.show()
