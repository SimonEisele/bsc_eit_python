import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


# ------------------------------
# 1. Funktion definieren
# ------------------------------
def f(x):
    return 5 * np.cos(2 * np.pi * x) * np.exp(-x)


# ------------------------------
# 2. x-Werte definieren (Einzelne Werte)
# ------------------------------
x1_vals = np.array([1, 1.1, 1.2, 1.3, 1.4, 1.5])

# ------------------------------
# 2. x-Werte definieren (Bestimmte Anzahl Werte linear verteilt über Bereich)
# ------------------------------
x2_vals = np.linspace(0, 2 * np.pi, 100)  # 100 Punkte zwischen -2 und 2

# ------------------------------
# 3. y-Werte berechnen
# ------------------------------
y1_vals = f(x1_vals)
y2_vals = f(x2_vals)

# ------------------------------
# 4. Funktionswerte der einzeln  bestimmten x-Werten ausgeben
# ------------------------------
for x, y in zip(x1_vals, y1_vals):
    print(f"x = {x:.2f}, f(x) = {y:.2f}")

# ------------------------------
# 5. 2D-Plot erstellen
# ------------------------------
plt.plot(x2_vals, y2_vals, label=r'$f(x) = 5 \cos(2\pi x) e^{-x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funktionswerte')
plt.grid(True)
plt.legend()

# ------------------------------
# 6. Plot als PNG speichern
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
