# Imports
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Définition des constantes
T = 2.3
omp = 2 * np.pi / T
Q = 5

# Fonction de l'oscillateur harmonique
def oscillateur(y, t):
    # On extrait les coordonnées
    theta, omega = y

    # On les dérive on fonction du temps
    dtheta = omega
    domega = -omp * omega / Q - omp**2 * theta
    return (dtheta, domega)

# Conditions initiales
y0 = (0.3, 0)
t = np.linspace(0, 5, 1001)

# On résout l'équa diff
solution = odeint(oscillateur, y0, t)

# On extrait les coordonnées
theta, omega = solution[:, 0], solution[:, 1]

# On trace
plt.title('θ et ω en fonction du temps')
plt.plot(t, theta, label="θ(t)")
plt.plot(t, omega, label="ω(t)")
plt.legend()
plt.show()
