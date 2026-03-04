import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

# Valores
x = np.linspace(-10, 10, 200)

# Parâmetros do sino
A = 1        # altura
mu = 0       # centro
sigma = 2    # largura

# Equação Gaussiana
y = A * np.exp(-((x - mu)**2) / (2 * sigma**2))

plt.scatter(x, y)
plt.plot(x, y)
plt.title("Curva em forma de sino (Gaussiana)")
plt.show()