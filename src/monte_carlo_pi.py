import numpy as np
import matplotlib.pyplot as plt
import math

num_points = 10000
np.random.seed(42)

x_points = np.random.rand(num_points)
y_points = np.random.rand(num_points)

inside_circle = (x_points**2 + y_points**2) <= 1

pi_values = 4 * np.cumsum(inside_circle) / np.arange(1, num_points + 1)


plt.figure(figsize=(10, 6))
plt.plot(pi_values, label="Monte Carlo π Estimate")
plt.axhline(math.pi, linestyle="--", color="red", label="True π")
plt.xlabel("Number of Points")
plt.ylabel("π Value")
plt.title("Monte Carlo Simulation for Estimating π")
plt.legend()
plt.grid(True)
plt.show()
