# -*- coding: utf-8 -*-
from matplotlib.pylab import *
from scipy.integrate import odeint

m = 1
f = 1
E = 0.2
w = 2*pi*f
k = m*(w**2)
c = 2*E*w*m

"""
Edo ... m*xpp + c*x + k*x = 0

CI... x(0) = 1 y xp(0) = 1


"""


def zp(z,t):
    zp = zeros(2)
    zp[0] = z[1]
    zp[1] = (-c*z[1]/m)+(-k*z[0]/m)
    
    return zp




def eulerint(zp, z0, t, Nsubdiv=1):
    Nt=len(t)
    Ndim= len(z0)
    
    z=zeros((Nt, Ndim))
    z[0,:]=z0
    
    for i in range(1, Nt):
        t_anterior=t[i-1]
        dt = (t[i]-t[i-1])/Nsubdiv
        z_temp=z[i-1,:].copy()
        
        for k in range(Nsubdiv):
            z_temp += dt*zp(z_temp, t_anterior + k*dt)
        
        z[i,:] = z_temp
        
    return z

z0 = [1,1]

t = linspace(0, 4, 100)

### Resolviendo la EDO y reemplazando con los valores de arriba se llega a la siguente expresion

A =1.06413   
phi = 2.7968

##### A y phi se obtienen de las condiciones iniciales
exponente = -c*t/(2*m)
y = -A*exp(exponente)*cos(w*t + phi)
z_real = y

sol = odeint(zp, z0, t)
odeint_sol =sol[:,0]

sol2 = eulerint(zp,z0,t, Nsubdiv =1)
sol3 = eulerint(zp,z0,t, Nsubdiv =10)
sol4 = eulerint(zp,z0,t, Nsubdiv =100)

eulerint_sol2 =  sol2[:,0]
eulerint_sol3 =  sol3[:,0]
eulerint_sol4 =  sol4[:,0]


plot(t,odeint_sol,"-",label="odeint", color="b")

plot(t,eulerint_sol2,"--", label="eulerint 1", color="g")
plot(t,eulerint_sol3,"--", label="eulerint 10", color="r")
plot(t,eulerint_sol4,"--", label="eulerint 100", color="orange")

plt.plot(t,z_real,"-",label="real",linewidth=2, color="black")

plt.title("Oscilador Armónico")
plt.ylabel("Amplitud (A)")
plt.xlabel("Tiempo (t)")

legend()
show()