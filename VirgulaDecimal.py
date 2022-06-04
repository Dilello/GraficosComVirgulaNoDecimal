#Locale settings
import locale
# Set to German locale to get comma decimal separater
locale.setlocale(locale.LC_NUMERIC, "de_DE")

import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

# Tell matplotlib to use the locale we set above
plt.rcParams['axes.formatter.use_locale'] = True

# make the figure and axes
fig,ax = plt.subplots(1)

# Some example data
x=np.arange(100)
y=4e-18*x**2

# plot the data
ax.plot(x,y,'b-')

plt.show()