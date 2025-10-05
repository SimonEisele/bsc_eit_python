import numpy as np

# ------------------------------
# 1. Matrix definieren
# ------------------------------
A = np.array([[-1, 1, 2],
              [3, -1, 1],
              [-1, 3, 4]], dtype=float)

B = np.array([10, -20, 40], dtype=float)  # rechte Seite des Gleichungssystems

print("Matrix A:")
print(A)
print("\nVektor B:")
print(B)

# ------------------------------
# 2. Lineares Gleichungssystem Ax = B lösen
# ------------------------------
x = np.linalg.solve(A, B)
print("\nLösung von Ax = B:")
print(x)

# ------------------------------
# 3. Determinante
# ------------------------------
det = np.linalg.det(A)
print("\nDeterminante von A:", det)
