# ------------------------------
# Template
# ------------------------------

# Bibliotheken importieren
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

# ------------------------------
# 1. Funktion definieren
# ------------------------------
# Symbolische Funktion
x, y = sp.symbols('x y')
f_sym = x**4 + y**2  # Beispiel: symbolische Funktion


# Numerische Version für Berechnungen
def f_num(x, y=0):
    """Numerische Version der Funktion."""
    return x**4 + y**2


# ------------------------------
# 2. Symbolische Berechnungen
# ------------------------------
df_dx = sp.diff(f_sym, x)
df_dy = sp.diff(f_sym, y)
integral_x = sp.integrate(f_sym, x)

print("Ableitung nach x:", df_dx)
print("Ableitung nach y:", df_dy)
print("Integral nach x:", integral_x)

# ------------------------------
# 3. Numerische Werte erzeugen
# ------------------------------
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f_num(X, Y)

# ------------------------------
# 4. 2D-Plot
# ------------------------------
plt.figure()
plt.plot(x_vals, f_num(x_vals))
plt.title("2D-Plot: f(x) = x^4 + 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# ------------------------------
# 5. Interaktiver 3D-Plot (Matplotlib)
# ------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D-Plot Matplotlib")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# ------------------------------
# 6. Datenanalyse-Beispiel (Pandas)
# ------------------------------
data = pd.DataFrame({
    'x': x_vals,
    'y': f_num(x_vals)
})
print("Erste 5 Zeilen der Daten:")
print(data.head())


# ------------------------------
# 7. Beispiel: Neue 3D-Funktion definieren und darstellen
# ------------------------------
def f_example(x, y):
    return np.sin(x) * np.cos(y)  # Neue Funktion


Z_example = f_example(X, Y)

# 3D-Plot Matplotlib für neue Funktion
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z_example, cmap='plasma')
ax2.set_title("Beispiel 3D-Funktion: f(x,y) = sin(x)*cos(y)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
plt.show()
