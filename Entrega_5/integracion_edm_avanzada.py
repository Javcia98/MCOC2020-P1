# -*- coding: utf-8 -*-
import scipy as sp
import numpy as np
from time import perf_counter
from scipy.integrate import odeint
from math import cos, sin, sqrt
from matplotlib.pylab import *
from leer_eof import leer_eof
from sys import argv

nombre_eof = argv[1]
t0 = perf_counter()
t, x, y, z, vx, vy, vz = leer_eof(nombre_eof)

hr = 3600

masaT = 5.972*(10**24)  # Kg
masaC = 2170            # Kg
Ω = 7.27*10**-5             # rads/s
G = 6.67408*(10**-11)   # m^3/(Kg*s^2)
R = 6371000             # m

def satelite_Js(z,t):
    
    
    
    θ = Ω*t                 # rads      
    
    Rotor = [[cos(θ),- sin(θ),0], [sin(θ),cos(θ),0], [0, 0, 1]]
    
    R_derivado =np.dot(Ω,[[-sin(θ),- cos(θ),0], [cos(θ),-sin(θ),0], [0, 0, 0]])
    
    R_derivado2 =np.dot((Ω**2),[[-cos(θ), sin(θ),0], [-sin(θ),-cos(θ),0],[0, 0, 0]])
    
    r = sqrt(np.dot(z[0:3],z[0:3]))
    
    J2 = 1.75553*(10**25)
    
    
    Fx = (6*(z[2]**2)-3*(z[0]**2+z[1]**2)/2)*J2*z[0]/r**7
    
    Fy = (6*(z[2]**2)-3*(z[0]**2+z[1]**2)/2)*J2*z[1]/r**7
    
    Fz = (3*(z[2]**2)-9*(z[0]**2+z[1]**2)/2)*J2*z[2]/r**7
    
    
    vector_J2 =sp.zeros(3)
    vector_J2[0:3] = [Fx, Fy, Fz]
    
    J3 = -2.61913*(10**29)
    
    Fx2 = (10*(z[2]**2)-15*(z[0]**2+z[1]**2)/2)*J3*z[0]*z[2]/r**9
    
    Fy2 = (10*(z[2]**2)-15*(z[0]**2+z[1]**2)/2)*J3*z[1]*z[2]/r**9
    
    Fz2 = (4*(z[2]**2)*((z[2]**2)-3*(z[0]**2+z[1]**2))+(3/2)*(z[0]**2+z[1]**2)**2)*J3/r**9
    
    
    vector_J3 =sp.zeros(3)
    vector_J3[0:3] = [Fx2, Fy2, Fz2]
    
    zp = sp.zeros(6)
    zp[0:3] = z[3:6]
    zp[3:6]=((-G*masaT*z[0:3])/(r**3))-np.dot(np.transpose(Rotor),(np.dot(R_derivado2,z[0:3])+2*np.dot(R_derivado,z[3:6]))) + vector_J2/masaC + vector_J3/masaC     
    
    return zp
"""
def satelite(z,t):
    
    
    
    θ = Ω*t                 # rads      
    
    Rotor = [[cos(θ),- sin(θ),0], [sin(θ),cos(θ),0], [0, 0, 1]]
    
    R_derivado =np.dot(Ω,[[-sin(θ),- cos(θ),0], [cos(θ),-sin(θ),0], [0, 0, 0]])
    
    R_derivado2 =np.dot((Ω**2),[[-cos(θ), sin(θ),0], [-sin(θ),-cos(θ),0],[0, 0, 0]])
    
    r = sqrt(np.dot(z[0:3],z[0:3]))
    
    
    zp = sp.zeros(6)
    zp[0:3] = z[3:6]
    zp[3:6]=((-G*masaT*z[0:3])/(r**3))-np.dot(np.transpose(Rotor),(np.dot(R_derivado2,z[0:3])+2*np.dot(R_derivado,z[3:6])))    
    
    return zp
"""
t2=sp.linspace(0, t[-1]-t[0], 9361 )



z0 =sp.zeros(6)
z0[0:6] = [x[0], y[0], z[0],vx[0],vy[0], vz[0]]


z1 =sp.zeros(6)
z1[0:6] =  [x[-1], y[-1], z[-1],vx[-1],vy[-1], vz[-1]]

t1 = perf_counter()

sol=odeint(satelite_Js, z0, t2)

x_o = sol[:,0]
y_o = sol[:,1]
z_o = sol[:,2]

      

z2 =  (sol[-1])  
  

diferencia = z2[0:3] - z1[0:3]
error_d = sqrt(np.dot(diferencia,diferencia))

print(error_d)

figure()

subplot(3,1,1)
plot(t,x,"-", label=" Real", color="g")
plot(t,x_o,"-", label=" Odeint", color="b")
plt.title("Posición")
plt.ylabel("X (Km)")
tricky = [-5000000, 0, 5000000]
tricky_txt = [-5000, 0, 5000]

trickx = [0,3600*5,3600*10, 3600*15, 3600*20, 3600*25]
trickx_txt = [0,5,10,15,20,25]
plt.yticks(tricky, tricky_txt)
plt.xticks(trickx, trickx_txt) 
subplot(3,1,2)
plot(t,y,"-", label=" Real", color="g")
plot(t,y_o,"-", label=" Odeint", color="b")
plt.ylabel("Y (Km)")
plt.yticks(tricky, tricky_txt)
plt.xticks(trickx, trickx_txt) 
subplot(3,1,3)
plot(t,z,"-", label=" Real", color="g")
plot(t,z_o,"-", label=" Odeint", color="b")
plt.xlabel("Tiempo, t(horas)")
plt.ylabel("Z (Km)")
plt.yticks(tricky, tricky_txt)
plt.xticks(trickx, trickx_txt) 
legend()
show()

t3 = perf_counter()
######################################################

t4 = perf_counter()
def eulerint(zp, z0, t, Nsubdiv=1):
    Nt=len(t)
    Ndim= len(z0)
    
    z=sp.zeros((Nt, Ndim))
    z[0,:]=z0
    
    for i in range(1, Nt):
        t_anterior=t[i-1]
        dt = (t[i]-t[i-1])/Nsubdiv
        z_temp=z[i-1,:].copy()
        
        for k in range(Nsubdiv):
            z_temp += dt*zp(z_temp, t_anterior + k*dt)
        
        z[i,:] = z_temp
        
    return z



sol2 = eulerint(satelite_Js, z0,t2, Nsubdiv =1)





x_e = sol2[:,0]
y_e = sol2[:,1]
z_e = sol2[:,2]


delta = sqrt((x_e-x_o)**2 + (y_e-y_o)**2 + (z_e-z_o)**2)
#delta2 = sqrt((x-x_o)**2 + (y-y_o)**2 + (z-z_o)**2)


X = np.dot(t2,1/3600)
Y = np.dot(delta,1/10000)

#X_e = np.dot(t2,1/3600)
#Y_e = np.dot(delta2,1/10000)

plot(X,Y,"-", color="b")
#plot(X_e,Y_e,"-", label=" Eulerint", color="r")

xlabel("Tiempo, t (horas)")
ylabel("Deriva (km)")
title(f"Distancia entre odeint y eulerint (km)")

t5 = perf_counter()







   