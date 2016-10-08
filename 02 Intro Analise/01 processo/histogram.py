
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

data = [1, 2, 1, 3, 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2]
plt.xlabel("Rótulo para o eixo x")
plt.ylabel("Rótulo para eixo y")
plt.title("Título do gráfico")

plt.hist(data, bins=20)
plt.show()


#x = np.arange(0, 5, 0.1);
#y = np.sin(x)
#plt.plot(x, y)
#plt.show()