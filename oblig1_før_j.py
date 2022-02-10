import plotly.graph_objects as go
import plotly.subplots as ps
import numpy as np

# Initialbetingelser:
v0 = 0
T = 10
m = 80
F = 400
rho = 1.293
A0 = 0.45
CD = 1.2
w = 3

dt = 0.01

n = int(T/dt)

t = []; a = []; v = []; r = [] # bruker r for bevegelse

v.append(v0); r.append(0); t.append(0)
i = 0
while r[i] < 100 and i < 2000:
    a.append((F-0.5*rho*CD*A0*(v[i]-w)**2)/m)

    v.append(v[i]+dt*a[i])
    r.append(r[i]+dt*v[i+1])
    t.append(t[i]+dt)

    i+=1

a.append((F-0.5*rho*CD*A0*(v[i]-w)**2)/m)

# Plotting:
fig = ps.make_subplots(rows=2, cols=2, subplot_titles=('Fart', 'Akselerasjon', 'Beveget avstand'),
    specs=[[{}, {}],
           [{"colspan": 2}, None]]) # Setter det slik at siste plot skal ta opp både posisjon row=2, col=1 og row=2, col=2

fig.add_trace(go.Scatter(x=t, y=v, name='Fart (m/s)'), row=1, col=1)
fig.add_trace(go.Scatter(x=t, y=a, name='Akselerasjon (m/s**2)'), row=1, col=2)
fig.add_trace(go.Scatter(x=t, y=r, name='Bevegelse (m)'), row=2, col=1)

for i in range(1, 4):
    fig['layout'][f'xaxis{i}']['title']='t (s)'

fig['layout']['yaxis1']['title']='fart (m/s)'; fig['layout']['yaxis2']['title']='akselerasjon (m/s^2)'; fig['layout']['yaxis3']['title'] = 'avstand (m)'


fig.show()

"""
Kjøreeksempel:
>> Python oblig1_før_j.py
Et vindu åpnes i nettleseren med 3 grafer, en for fart, en for akselerasjon og en for avstand som sprinteren har løpt
"""
