import numpy as np
import matplotlib.pyplot as plt
t = np.arange (0.0, 20.0, 1.0)
plt.plot (t, 1997+t, 'g--')
plt.ylabel('anio')
plt.xlabel('edad')
plt.title('Joseph_Edrei_Moreno_Cruz')
plt.savefig('Pregunta1.png')
plt.show()
