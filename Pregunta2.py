import numpy as np
import matplotlib.pyplot as plt
def f(t):
  return np.cos(2015+t)

t1 = np.arange (0.0, 15.0, 0.1)
plt.plot (t1, 2*f(t1), 'y-.')
plt.title('Segunda pregunta del examen')
plt.savefig('Pregunta2.png')
plt.show()
