# Imports
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Déclaration de la courbe
teta = np.linspace(0, 2 * pi)
ep = 1 * (1 - np.cos(teta))

# Affichage du graphique
plt.title('Ep en fonction de θ')
plt.plot(teta, ep)
plt.show()
