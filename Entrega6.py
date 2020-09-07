# -*- coding: utf-8 -*-
import scipy as sp
import numpy as np
from scipy.integrate import odeint
from math import cos, sin, sqrt
from leer_eof import leer_eof
from sys import argv


nombre_eof = argv[1]
#nombre_eof = "S1A_OPER_AUX_POEORB_OPOD_20200823T121210_V20200802T225942_20200804T005942.EOF"
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
    zp[0:3] = z[3:6] + vector_J2*t/masaC + vector_J3*t/masaC
    zp[3:6]=((-G*masaT*z[0:3])/(r**3))-np.dot(np.transpose(Rotor),(np.dot(R_derivado2,z[0:3])+2*np.dot(R_derivado,z[3:6]))) + vector_J2/masaC + vector_J3/masaC     
    
    return zp

z0 =sp.zeros(6)
z0[0:6] = [x[0], y[0], z[0],vx[0],vy[0], vz[0]]

t2=sp.linspace(0, t[-1]-t[0], 9361)

sol=odeint(satelite_Js, z0, t2)

x_o = sol[:,0]
y_o = sol[:,1]
z_o = sol[:,2]
vx_o = sol[:,3]
vy_o = sol[:,4]
vz_o = sol[:,5]

nuevo_arch = open(nombre_eof)


name = (f"S1A_OPER_AUX_POEORB_OPOD_20200823T121210_V20200802T225942_20200804T005942.PRED")  #aqui se pone el nombre del archivo 

fid = open(name,"w")

i = 0

for linea in nuevo_arch:
    
    
    if linea[0:8]=="      <X":
        fid.write(f"      <X unit=\"m\">{x_o[i]}</X>\n")
        continue
    
    if linea[0:8]=="      <Y":
        fid.write(f"      <Y unit=\"m\">{y_o[i]}</Y>\n")
        continue
    
    if linea[0:8]=="      <Z":
        fid.write(f"      <Z unit=\"m\">{z_o[i]}</Z>\n")
        continue
    
    if linea[0:9]=="      <VX":
        fid.write(f"      <VX unit=\"m/s\">{vx_o[i]}</VX>\n")
        continue
    
    if linea[0:9]=="      <VY":
        fid.write(f"      <VY unit=\"m/s\">{vy_o[i]}</VY>\n")
        continue
    
    if linea[0:9]=="      <VZ":
        fid.write(f"      <VZ unit=\"m/s\">{vz_o[i]}</VZ>\n")
        i+=1
        continue
    
    
    else:
        fid.write(f"{linea}")
        continue

        
     
    fid.flush()





























