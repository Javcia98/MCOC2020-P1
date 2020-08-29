# -*- coding: utf-8 -*-
import scipy as sp
import numpy as np
from scipy.integrate import odeint
from math import cos, sin, sqrt
import matplotlib.pylab as plt

hr = 3600


masaT = 5.972*(10**24)  # Kg
masaC = 2170            # Kg
Ω = 7.27*10**-5             # rads/s
G = 6.67408*(10**-11)   # m^3/(Kg*s^2)
R = 6371000             # m

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





import datetime as dt

utc_EOFformat = "%Y-%m-%dT%H:%M:%S.%f"
t1 = dt.datetime.strptime("2020-08-02T22:59:42.000000",utc_EOFformat)
t2 = dt.datetime.strptime("2020-08-04T00:59:42.000000",utc_EOFformat)


"""
Ejemplo profesor
t1 = dt.datetime.strptime("2018-08-14T22:59:42.000000",utc_EOFformat)
t2 = dt.datetime.strptime("2018-08-16T00:59:42.000000",utc_EOFformat)
"""
intervalo = t2 - t1
intervalo_en_sec = intervalo.total_seconds()




t=sp.linspace(0, intervalo_en_sec,1001 )

z0=[-1957982.294674, 4247020.991834, 5300605.746747, -528.165617,5818.733943,-4845.325459]
"""
Ejemplo profesor
z0 =[ 2083293.582654,
  -6380690.028717,
  -2250417.463178,
  -805.237768, 
  -2737.127661,
  7035.393528]
"""
sol=odeint(satelite, z0, t)


"""    
#INICIO
<TAI>TAI=2020-08-02T23:00:19.000000</TAI>
<UTC>UTC=2020-08-02T22:59:42.000000</UTC>
<UT1>UT1=2020-08-02T22:59:41.793861</UT1>
<Absolute_Orbit>+33734</Absolute_Orbit>
<X unit="m">-1957982.294674</X>
<Y unit="m">4247020.991834</Y>
<Z unit="m">5300605.746747</Z>
<VX unit="m/s">-528.165617</VX>
<VY unit="m/s">5818.733943</VY>
<VZ unit="m/s">-4845.325459</VZ>

#FIN
<TAI>TAI=2020-08-04T01:00:19.000000</TAI>
<UTC>UTC=2020-08-04T00:59:42.000000</UTC>
<UT1>UT1=2020-08-04T00:59:41.794773</UT1>
<Absolute_Orbit>+33750</Absolute_Orbit>
<X unit="m">-1769951.165307</X>
<Y unit="m">-3398373.853807</Y>
<Z unit="m">5938697.226400</Z>
<VX unit="m/s">818.456869</VX>
<VY unit="m/s">6443.634448</VY>
<VZ unit="m/s">3922.189779</VZ>
"""      
z1=[-1769951.165307, -3398373.853807, 5938697.226400,
    818.456869, 6443.634448, 3922.189779]
"""
Ejemplo profesor
z1 =[ 1010095.475188,
  -123073.229951,
  -7008913.872221,
  -1887.279838,
  -7324.093741,
  -143.308102]
"""
z2 =  (sol[-1])    

diferencia = z0 - z2
error_d = sqrt(np.dot(diferencia,diferencia))

print(error_d)
   



















    
    