#Importa biblioteca locale
import locale

# Configura como vírgula o separado decimal e ponto como separador de milhar
locale.setlocale(locale.LC_NUMERIC, "de_DE")

import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

# Implementando a configuração no seu código
plt.rcParams['axes.formatter.use_locale'] = True

# Exemplo de gráfico nesta configuração:
fig,ax = plt.subplots(1)

x=np.arange(100)
y=4e-18*x**2

# Resultado:
ax.plot(x,y,'b-')

plt.show()
