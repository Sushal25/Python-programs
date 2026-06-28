import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34      # Planck's constant (J.s)
m = 9.109e-31      # Mass of electron (kg)

# User Inputs
L = float(input("Enter the length of the box L (in meters): "))
n = int(input("Enter the quantum number n (1,2,3,...): "))

# Position values inside the box
x = np.linspace(0, L, 1000)

# Wave Function ψ(x)
psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Probability Density |ψ(x)|²
prob_density = psi**2

# Energy of nth state
E = (n**2 * h**2) / (8 * m * L**2)

print(f"\nEnergy of the particle in state n={n}:")
print(f"E = {E:.3e} Joules")

# Plotting
plt.figure(figsize=(10, 5))

# Wave Function Plot
plt.subplot(1, 2, 1)
plt.plot(x, psi)
plt.title(f"Wave Function ψ(x) for n={n}")
plt.xlabel("Position x (m)")
plt.ylabel("ψ(x)")
plt.grid(True)

# Probability Density Plot
plt.subplot(1, 2, 2)
plt.plot(x, prob_density)
plt.title(f"Probability Density |ψ(x)|² for n={n}")
plt.xlabel("Position x (m)")
plt.ylabel("|ψ(x)|²")
plt.grid(True)

plt.tight_layout()
plt.show()