import numpy as np

# Coefficients of the cubic equation
coefficients = [1, -1, 24, 8]

# Find roots of the cubic equation
roots = np.roots(coefficients)
print("Roots of the cubic equation:", roots)