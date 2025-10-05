import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


# ------------------------------
# 1. Funktion: Zwischenwinkel berechnen
# ------------------------------
def getZwischenwinkel(a, b, deg=False):
    a = np.array(a)
    b = np.array(b)
    cos_theta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta = np.arccos(cos_theta)
    if deg:
        theta = np.degrees(theta)
    return theta


# ------------------------------
# 2. Funktion: Vektoren plotten und Winkel anzeigen
# ------------------------------
def plotVectors():
    try:
        # Vektoren aus GUI einlesen
        a = [float(entry_a_x.get()), float(entry_a_y.get()),
             float(entry_a_z.get())]
        b = [float(entry_b_x.get()), float(entry_b_y.get()),
             float(entry_b_z.get())]
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")
        return

    # Winkel berechnen
    winkel_rad = getZwischenwinkel(a, b)
    winkel_deg = getZwischenwinkel(a, b, deg=True)

    messagebox.showinfo("Zwischenwinkel",
                        f"Winkel in Radiant: {winkel_rad:.4f} rad\n"
                        f"Winkel in Grad: {winkel_deg:.2f}°\n")

    # ------------------------
    # 3D-Plot erstellen
    # ------------------------
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Pfeile vom Ursprung
    ax.quiver(0, 0, 0, a[0], a[1], a[2], color='blue', linewidth=2,
              arrow_length_ratio=0.1, label='a')
    ax.quiver(0, 0, 0, b[0], b[1], b[2], color='red', linewidth=2,
              arrow_length_ratio=0.1, label='b')

    # Ursprung
    ax.scatter(0, 0, 0, color='black', s=20)

    # Achsenbeschriftung
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Limits
    max_range = max(np.linalg.norm(a), np.linalg.norm(b)) + 1
    ax.set_xlim([0, max_range])
    ax.set_ylim([0, max_range])
    ax.set_zlim([0, max_range])

    # Legende und Titel
    ax.legend()
    ax.set_title(f"3D Vektoren, Winkel: {winkel_deg:.1f}°")

    plt.show()


# ------------------------------
# 3. GUI aufbauen
# ------------------------------
root = tk.Tk()
root.title("3D Vektoren und Zwischenwinkel")

# Labels und Eingaben für Vektor A und B
labels = ['x', 'y', 'z']
tk.Label(root, text="Vektor A:").grid(row=0, column=0)
entry_a_x = tk.Entry(root)
entry_a_x.grid(row=0, column=1)
entry_a_y = tk.Entry(root)
entry_a_y.grid(row=0, column=2)
entry_a_z = tk.Entry(root)
entry_a_z.grid(row=0, column=3)

tk.Label(root, text="Vektor B:").grid(row=1, column=0)
entry_b_x = tk.Entry(root)
entry_b_x.grid(row=1, column=1)
entry_b_y = tk.Entry(root)
entry_b_y.grid(row=1, column=2)
entry_b_z = tk.Entry(root)
entry_b_z.grid(row=1, column=3)

# Button zum Plotten
tk.Button(root, text="Zwischenwinkel berechnen",
          command=plotVectors).grid(row=2,
                                    column=0,
                                    columnspan=4)

root.mainloop()
