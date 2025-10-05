import numpy as np
import matplotlib.pyplot as plt


# ------------------------------
# 1. Funktion definieren
# ------------------------------
def zwischenwinkel(a, b, deg=False):
    """
    Berechnet den Zwischenwinkel zwischen zwei Vektoren a und b.

    Parameter:
        a, b : list oder np.array
            Vektoren (beliebige Dimension)
        deg : bool
            True -> Winkel in Grad, False -> Winkel in Radiant

    Rückgabe:
        Winkel zwischen a und b
    """
    a = np.array(a)
    b = np.array(b)

    # Skalarprodukt und Normen
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # cos(theta)
    cos_theta = dot_product / (norm_a * norm_b)

    # numerische Stabilität: cos_theta in [-1,1] begrenzen
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Winkel berechnen
    theta = np.arccos(cos_theta)

    if deg:
        theta = np.degrees(theta)

    return theta


# ------------------------
# 2. Funktion aufrufen mit zwei Vektoren
# ------------------------
a = [100, 6, 3]
b = [10, 9, 2]

winkel_rad = zwischenwinkel(a, b)
winkel_deg = zwischenwinkel(a, b, deg=True)

print(f"Winkel in Radiant: {winkel_rad:.4f}")
print(f"Winkel in Grad: {winkel_deg:.2f}")

# ------------------------
# 3. 3D-Plot erstellen
# ------------------------
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

# Pfeile vom Ursprung
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='blue', linewidth=2,
          arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='red', linewidth=2,
          arrow_length_ratio=0.1)

# Ursprung
ax.scatter(0, 0, 0, color='black', s=20)

# Achsenbeschriftung
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Limits (automatisch passend)
max_range = max(np.linalg.norm(a), np.linalg.norm(b)) + 1
ax.set_xlim([0, max_range])
ax.set_ylim([0, max_range])
ax.set_zlim([0, max_range])

# Legende und Titel
ax.legend()
ax.set_title(f"3D Vektoren, Winkel: {winkel_deg:.1f}°")

plt.show()
