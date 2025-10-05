import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


# ------------------------------
# 1. Funktion definieren
# ------------------------------
def f(x, y):
    return np.sin(x**2-y**2)


# ------------------------------
# 2. x- und y-Werte definieren (Einzelne Werte)
# ------------------------------
x1_vals = np.array([-1, 0, 1, 2, 3])
y1_vals = np.array([0, 1, 2, 3, 4,])

# ------------------------------
# 2. x- und y-Werte definieren (Werte linear verteilt über Bereich)
# ------------------------------
x2_vals = np.linspace(-2, 2, 40)  # 40 Punkte zwischen -2 und 2
y2_vals = np.linspace(-1, 3, 40)  # 40 Punkte zwischen -1 und 3

# ------------------------------
# 3. 2D-Gitter erstellen (Für plot)
# ------------------------------
X2, Y2 = np.meshgrid(x2_vals, y2_vals)

# ------------------------------
# 4. y-Werte berechnen
# ------------------------------
z1_vals = f(x1_vals, y1_vals)
Z2 = f(X2, Y2)

# ------------------------------
# 5. Funktionswerte der einzeln bestimmten x- und y-Werten ausgeben
# ------------------------------
for x, y, z in zip(x1_vals, y1_vals, z1_vals):
    print(f"x = {x:.2f}, y = {y:.2f}, f(x, y) = {z:.2f}")

# ------------------------------
# 6. 3D-Plot erstellen
# ------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X2, Y2, Z2, cmap='viridis')
ax.set_title("3D-Plot Matplotlib")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# ------------------------------
# 7. Plot als PNG speichern
# ------------------------------
root = Tk()
root.withdraw()  # Hauptfenster von Tkinter ausblenden

# Dateidialog öffnen
speicherort = asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    title="Speicherort für Plot auswählen",
    initialfile="function01.png"
)

if speicherort:  # Wenn ein Speicherort gewählt wurde
    plt.savefig(speicherort, dpi=300)
    print(f"Plot gespeichert unter: {speicherort}")
else:
    print("Speichern abgebrochen.")

# ------------------------------
# 7. 2D-Plot anzeigen
# ------------------------------
plt.show()
