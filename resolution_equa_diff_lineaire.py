# Imports
from scipy.integrate import odeint
from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt

# Définition des constantes
T0 = 1
t = np.linspace(0, 5, 1001)

# Fonction qui dérive
def derive(y, t):
    # On extrait les coordonnées
    theta, omega = y

    # On les dérive on fonction du temps
    dtheta = omega
    domega = (-4 * pi ** 2 * sin(theta)) / (T0 ** 2)
    return (dtheta, domega)

# Fonction qui résoud l'équa diff selon les conditions initiales
def resoudre(theta0, omega0):
    # Conditions initiales
    y0 = (theta0, omega0)

    # On résout l'équa diff
    solution = odeint(derive, y0, t)

    # On extrait les coordonnées
    theta = solution[:, 0]

    # On retourne theta
    return theta

# On applique
theta1 = resoudre(0.1, 0)
theta2 = resoudre(0.5, 0)
theta3 = resoudre(1, 0)

# On trace
plt.title('θ en fonction du temps')
plt.plot(t, theta1, label="θ0 = 0.1 rad")
plt.plot(t, theta2, label="θ0 = 0.5 rad")
plt.plot(t, theta3, label="θ0 = 1 rad")
plt.legend()
plt.show()
