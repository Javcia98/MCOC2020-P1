# MCOC2020-P1

![alt text](https://github.com/Javcia98/MCOC2020-P1/blob/master/Entrega%201/Grafico1.png)

# Entrega 4
![alt text](https://github.com/Javcia98/MCOC2020-P1/blob/master/Grafico%20metodos.png) <br>
Se puede ver claramente que las curvas odeint,eulerint 10 , eulerint 100 y real son muy parecidas, esto se debe a que la primera y la ultima son prácticamente la solución exacta. Al contrario, las soluciones eulerint tienen la particularidad de que al aumentar el numero de subdivisiones esta curva se hace mas exacta llegado a ser casi idéntica a las correcta con 100 subdivisiones. Estas subdivisiones determinan el tamaño del paso del tiempo para su curva correspondiente por lo que claramente si se usa una subdivisión pequeña entonces el paso del tiempo sera mayor y se perderá exactitud, fenómeno que se observa a la perfección en la gráfica.

# Entrega 5
Pregunta 1:<br>
![alt text](https://github.com/Javcia98/MCOC2020-P1/blob/master/Entrega_5/G-1%20(1).png)<br>
 

Pregunta 2: <br>
![alt text](https://github.com/Javcia98/MCOC2020-P1/blob/master/Entrega_5/G-2%20(2).png) <br>

El eulerint deriva del odeint al final de tiempo en : 19801.760 km  <br>
Tiempo de:  <br>
odeint --> 1.061 s <br>
eulerint --> 1.301 s <br>



Pregunta 3: Al hacer correr mi codigo aumentando el numero de subdivisiones se vio una disminucion considerable en la distancia del eulerint con el odeint. Lamentablemente al llegar a alrededor de 1000 subdivisiones el programa se demoraba demasiado como para seguir aumentandolo por lo que no me fue posible llegar al 1% de error. Pero aprendi que si se aumenta el numero de subdivisiones la deriva disminuye considerablemente.<br>

Pregunta 4:  Con la implementacion  CORRECTA de J2 y J3 <br>
1. <br>
![alt text](https://github.com/Javcia98/MCOC2020-P1/blob/master/Entrega_5/G-1J%20(1).png) <br>
 

2.  <br>
![alt text](https://github.com/Javcia98/MCOC2020-P1/blob/master/Entrega_5/G-2J%20(2).png) <br>

Los dos graficos son practicamente iguales a los con la implementacion (pasada) erronea de J2 y J3, pero la deriva tuvo un cambio positivo. <br>

El eulerint deriva del odeint al final de tiempo en :  De 19801.262 km   pasó a 19366.490 km de deriva... Una gran reduccion del distancia!<br>
En relacion con el tiempo de ejecucion, los cambios fueron los siguientes:  <br>
odeint --> 1.426 s   a    2.131 s <br>
                          
eulerint --> 2.715 s  a   1.289 s <br>
Una claro aumento en el tiempo de odeint y una reduccion en eulerint <br>
3. Al hacer correr mi codigo aumentando el numero de subdivisiones se vio una disminucion considerable en la distancia del eulerint con el odeint. Lamentablemente al llegar a alrededor de 1000 subdivisiones el programa se demoraba demasiado como para seguir aumentandolo por lo que no me fue posible llegar al 1% de error. Pero aprendi que si se aumenta el numero de subdivisiones la deriva disminuye considerablemente. <br>
4. El codigo se demora:  7.415 s  a  3.420 s .... Gran mejora! por lo que se llega a la conclusion de que la nueva implementacion de J2 y J3 es bastamente mejor que la anterior.
