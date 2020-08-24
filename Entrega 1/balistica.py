# -*- coding: utf-8 -*-
import scipy as sp
from scipy.integrate import odeint

def balistica (V):
    #Uidades Base:
 
    cm = 0.01  # en metros
    inch = 2.45*cm    
    m = 15  # kg 
    # Coef de arrastre

    p = 1.225  #kg/m^3
    cd = 0.47
    D = 8.5*inch
    r = D/2
    A = sp.pi*r**2
    CD = 0.5*p*cd*A

    g = 9.81  # m/s**2

    # Funcion a integrar:
        # z es el vector de estado   z = [x, y, vx, vy]    
        # dz/dt =[z2      ]
        #        [        ]
        #        [FD/m  -g]

    # Vector de estado: z[0] = x; z[1] = y; z[2] = vx
    

    def bala (z,t):   
        zp = sp.zeros(4)
        zp[0] = z[2]
        zp[1] = z[3]
        v = z[2:4]
        v[0] = v[0] -V
        v2 = sp.dot(v,v)
        vnorm = sp.sqrt(v2)
        FD = -CD*v2*(v/vnorm)
        zp[2] = FD[0]/m
        zp[3] = FD[1]/m - g
    
        return zp

    # vector de tiempo
    t = sp.linspace(0, 30, 1001)
    vi = 100*1000/3600
    z0 = sp.array([0,0,vi,vi])

    # Parte en el origen y tiene vx=vy= 2 m/s

    sol = odeint (bala, z0, t)
    return sol

import matplotlib.pylab as plt

sol = balistica(0)
x = sol[:,0]
y = sol[:,1]

sol2 = balistica(10)
x2 = sol2[:,0]
y2 = sol2[:,1]

sol3 = balistica(20)
x3 = sol3[:,0]
y3 = sol3[:,1]

plt.figure(1)

plt.plot(x,y, color='b')
plt.plot(x2,y2,color='orange')
plt.plot(x3,y3,color='g')
plt.axis([0,150,0,50])
plt.grid(True)

plt.legend(('V = 0 m/s', 'V = 10.0 m/s', "V = 20.0 m/s" 
            ),prop = {'size': 10}, loc='upper right')


trickx = [0,20,40,60,80 ,100, 120, 140]
trickx_txt = [0,20,40,60,80 ,100, 120, 140]
plt.xticks(trickx, trickx_txt)

tricky = [0,10,20,30,40 ,50]
tricky_txt = [0,10,20,30,40 ,50]
plt.yticks(tricky, tricky_txt)


plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title("Trayectoria para distintos vientos")

plt.savefig(f"Grafico{1}.png")
       
plt.close(1)    
    
    
    
    
    
    
    
    
    