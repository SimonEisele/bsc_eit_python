import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


# ------------------------------
# 1. Funktion definieren
# ------------------------------
def drawTriangle(a, b, c):
    # Mittelpunkte berechnen
    m_ab = [(a[0]+b[0])/2, (a[1]+b[1])/2]
    m_bc = [(b[0]+c[0])/2, (b[1]+c[1])/2]
    m_ca = [(c[0]+a[0])/2, (c[1]+a[1])/2]

    # Subplots vorbereiten (1 Zeile, 2 Spalten)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # ------------------------------
    # Plot 1: Ursprüngliches Dreieck mit Seitenhalbierenden
    # ------------------------------
    ax1.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]],
             color='gray',
             alpha=0.3,
             label='Dreiecksfläche')
    ax1.plot([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]], 'k-',
             linewidth=2,
             label='Dreiecksseiten')

    # Seitenhalbierenden
    ax1.plot([a[0], m_bc[0]], [a[1], m_bc[1]], 'r--',
             label='Seitenhalbierenden')
    ax1.plot([b[0], m_ca[0]], [b[1], m_ca[1]], 'r--')
    ax1.plot([c[0], m_ab[0]], [c[1], m_ab[1]], 'r--')

    # Punkte markieren
    ax1.scatter([a[0], b[0], c[0]], [a[1], b[1], c[1]], color='black')

    ax1.set_title('Dreieck mit Seitenhalbierenden')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.axis("equal")
    ax1.grid(True)
    ax1.legend()

    # ------------------------------
    # Plot 2: Dreieck aus Seitenhalbierenden
    # ------------------------------
    ax2.fill(
        [0, (b[0]+c[0])/2 - a[0], c[0] - (a[0]+b[0])/2],
        [0, (b[1]+c[1])/2 - a[1], c[1] - (a[1]+b[1])/2],
        color='orange', alpha=0.4, label='Dreieck aus Seitenhalbierenden'
    )
    ax2.plot(
        [0, (b[0]+c[0])/2 - a[0], c[0] - (a[0]+b[0])/2, 0],
        [0, (b[1]+c[1])/2 - a[1], c[1] - (a[1]+b[1])/2, 0],
        'k-', linewidth=2
    )

    ax2.set_title('Mittendreieck aus Seitenhalbierenden')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.axis("equal")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()


# ------------------------------
# 2. Funktion für Aufruf aus GUI definieren
# ------------------------------
def readPointsAndDrawTriangles():
    # Punkte einlesen
    try:
        # Eingabe aus GUI-Feldern lesen
        a = [float(entry_a_x.get()), float(entry_a_y.get())]
        b = [float(entry_b_x.get()), float(entry_b_y.get())]
        c = [float(entry_c_x.get()), float(entry_c_y.get())]
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")
        return
    drawTriangle(a, b, c)


# ------------------------------
# 2. GUI aufbauen
# ------------------------------
root = tk.Tk()
root.title("Dreieck mit Seitenhalbierenden")

# Labels und Eingaben für die Punkte
points = ['A', 'B', 'C']
entries = []
for i, p in enumerate(points):
    tk.Label(root, text=f"{p} x:").grid(row=i, column=0)
    tk.Label(root, text=f"{p} y:").grid(row=i, column=2)
    entry_x = tk.Entry(root)
    entry_x.grid(row=i, column=1)
    entry_y = tk.Entry(root)
    entry_y.grid(row=i, column=3)
    entries.append((entry_x, entry_y))

entry_a_x, entry_a_y = entries[0]
entry_b_x, entry_b_y = entries[1]
entry_c_x, entry_c_y = entries[2]

# Button zum Plotten
tk.Button(root, text="Plot Dreieck",
          command=readPointsAndDrawTriangles).grid(row=3,
                                                   column=0,
                                                   columnspan=4)

root.mainloop()
