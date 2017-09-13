import numpy as np
import matplotlib.pyplot as plt

def f(t):
  return np.cos(2015+t)

t1 = np.arange(0.0, 15.0, 0.1)
t2 = np.arange(0.0, 15.0, 0.1)

plt.figure(1)

plt.subplot(211)

plt.plot(t1, 1997+t1, 'mx', t2, 2*f(t1)+1997, 'k--')
#Note que no es la trigonometrica tal como la pidio, sin embargo, tal como explique en la pregunta 3, la he modificado para que luzca mejor
plt.subplot(212)
plt.plot(t2, 2*f(t2), 'r')
plt.savefig('Pregunta3.png')
plt.show()
