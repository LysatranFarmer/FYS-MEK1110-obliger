import numpy as np

import matplotlib.pyplot as plt

# Initialbetingelser:
L0 = 1
e1 = np.array([1, 0])
e2 = np.array([0, 1])
y0 = np.sqrt(3)/2
x0 = 1/2
g = 9.81

T = 10
dt = 0.001
n = int(T/dt)
t = np.zeros(n+1); x = np.zeros(n+1); y = np.zeros(n+1)

r = np.zeros([n+1, 2]); v = np.zeros([n+1, 2]); a = np.zeros([n+1, 2]) # skaper arrayer med dimensjon høyde n+1 og bredde 2

# Initialbetingelser for arrayer:
x[0] = x0; y[0] = y0
r[0] = x0 * e1 + y0 * e2
a[0] = -2000*(np.linalg.norm(r[0, :])-L0) * r[0]/np.linalg.norm(r[0, :])  - g*e2
v[0] = [0, 0]

for i in range(n):
    r_len = np.linalg.norm(r[i, :])
    a[i+1] = 2000*(r_len-L0)*-r[i]/r_len - g*e2

    v[i+1] = v[i] + dt*a[i]

    # Regner ut bevegelsen komponentvis:
    x[i+1] = x[i] + dt*v[i][0]
    y[i+1] = y[i] + dt*v[i][1]
    # Legger til komponentene av bevegelsen til bevegelsesarrayen r
    r[i+1] = x[i+1]*e1 + y[i+1]*e2
    t[i+1] = t[i]+dt

print(r)
plt.plot(x,y)
plt.show()
