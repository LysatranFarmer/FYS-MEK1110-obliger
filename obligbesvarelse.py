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
w = 0         # Vindhastighet
tc = 0.67     # Tiden hvor sprinter ikke lenger er sammenkrøpet
fv = 25.8
fc = 488

dt = 0.01

n = int(T/dt)

t = []; a = []; v = []; r = [] # I større programmer ville vært fordelmessig å bruke np.zeros her, men for å unngå å måtte gå igjennom arrayene og
                               # fjerne alle nullverdiene løser jeg det heller på denne måten.

def A(t):
    return A0*(1-0.25*np.exp(-(t/tc)**2))

def FC(t):
    return fc*np.exp(-(t/tc)**2)

v.append(v0); r.append(0); t.append(0)
i = 0
while r[i] < 100 and i < 2000: # Hvis sprinteren ikke når 100 meter på maks verdi for i, er det bare å øke den så mye man ønsker
    a.append(F + FC(t[i]) - fv*v[i] - 0.5*rho*CD*A(t[i])*(v[i]-w)**2) # NB: a vil alltid være én indeks bak v, r og t i denne while løkken

    v.append(v[i]+dt*a[i])
    r.append(r[i]+dt*v[i+1])
    t.append(t[i]+dt)

    i += 1

a.append(F + FC(t[i]) - fv*v[i] - 0.5*rho*CD*A(t[i])*(v[i]-w)**2) # Regner ut a[i+1], for at a, v, r, t alle skal ha i+1 verdier i sine lister

# Plotting:
fig = ps.make_subplots(rows=2, cols=2, subplot_titles=('Fart', 'Akselerasjon', 'Beveget avstand'),
    specs=[[{}, {}],
           [{"colspan": 2}, None]]) # Setter det slik at siste plot skal ta opp både posisjon row=2, col=1 og row=2, col=2

# Legg til plots i subplottene
fig.add_trace(go.Scatter(x=t, y=v, name='fart (m/s)'), row=1, col=1, )
fig.add_trace(go.Scatter(x=t, y=a, name='Akselerasjon (m/s**2)'), row=1, col=2)
fig.add_trace(go.Scatter(x=t, y=r, name='Bevegelse (m)'), row=2, col=1)

#Legger til navn til akser:
for i in range(1, 4):
    fig['layout'][f'xaxis{i}']['title']='t (s)'

fig['layout']['yaxis1']['title']='fart (m/s)'; fig['layout']['yaxis2']['title']='akselerasjon (m/s^2)'; fig['layout']['yaxis3']['title'] = 'avstand (m)'

fig.show()

"""
Kjøreeksempel:
>> python obligbesvarelse.py
Et vindu åpnes i nettleseren med 3 grafer, en for fart, en for akselerasjon og en for avstand som sprinteren har løpt
"""
