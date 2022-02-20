import numpy as np
import matplotlib.pyplot as plt


# Create X,Y Graph 
x = np.linspace(0,5,20)
y = np.linspace(0,10,20)

plt.plot(x,y,'purple') # lines
plt.plot(x,y,'o') # dots

# Create X,Y,Z 3d graph
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
X = np.arange(-5,5,0.15)
Y = np.arange(-5,5,0.15)
X, Y = np.meshgrid(X,Y)

R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z, rstride =1, cstride=1, cmap='viridis')
plt.show()