# -*- coding: utf-8 -*-
import scipy as sp
import numpy as np
from scipy.integrate import odeint
from math import cos, sin

def satelite(z,t):
    masaT = 5.972*(10**24)  # Kg
    masaC = 2170            # Kg
    Ω = 7.27*10**-5             # rads/s
    G = 6.67408*(10**-11)   # m^3/(Kg*s^2)
    R = 6371000             # m
    
    θ = Ω*t                 # rads      
    
    
    Rotor = [[cos(θ),- sin(θ),0], [sin(θ),cos(θ),0], [0, 0, 1]]
    
    R_derivado =np.dot(Ω,[[-sin(θ),- cos(θ),0], [cos(θ),-sin(θ),0], [0, 0, 0]])
    
    R_derivado2 =np.dot((Ω**2),[[-cos(θ), sin(θ),0], [-sin(θ),-cos(θ),0],[0, 0, 0]])
    
    r = 7071000
    #r =(np.dot(z[0:3],z[0:3]))**2 + R
    
    zp = sp.zeros(6)
    zp[0:3] = z[3:6]
    zp[3:6]=((-G*masaT*z[0:3])/(r**3))-np.dot(np.transpose(Rotor),(np.dot(R_derivado2,z[0:3])+2*np.dot(R_derivado,z[3:6])))
    
    return zp

t=sp.linspace(0, 14400, 14401)
z0=[7071000,0,0,0,6500,0]
sol=odeint(satelite, z0, t)













    
    