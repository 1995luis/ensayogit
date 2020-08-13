# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#problemas secuenciales

'''Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto
dinero ganara después de un mes si el banco paga a razón de 2% mensual.'''
capinv=int(input("ingrese su capital invertido"))
gan=capinv * 0.02
print(f"la ganancia total es de:  {gan}")

'''Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
base y comisiones.'''
sb:int(input("ingrese el sueldo base"))
v1=float(input("ingrese el total de la venta1"))
venta2=int(input("ingrese el total de la venta2"))
venta3=float(input("ingrese el total de la venta3"))

tot_vta=(v1+venta2+venta3)
com=tot_vta*0.10
tpag=tot_vta+com

print(f"el total de las compras:{com}")
print(f"el total  a pagar  es  de :{tpag}")
'''Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuanto deberá pagar finalmente por su compra.'''
compratotal=int(input("ingrese el total de la compra"))
des=compratotal*0.15
tot_pag=compratotal - des
print(f"total a pagar es :{tot_pag}")
'''Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.'''
c1=float(input("ingrese calificacion uno"))
c2=float(input("ingrese calificacion dos "))
c3=float(input("ingrese calificacion tres "))
ef=float(input("ingrese examen final"))
tf=float(input("ingrese  trabajo final"))
prom=(c1+c2+c3)/3
ppar=-prom*0.55
pef=ef*0.30
ptf=tf*0.15
cf=ppar+pef+ptf
print(f"la calificacion final es :{cf}")

'''Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres hay en
un grupo de estudiantes.'''
nm=int(input("ingrese cantidad de mujeres"))
nh=int(input("ingrese cantidad de hombres"))
total=nh+nm
phom=nh*100/total
pmu=nm*100/total
print(f"el promdeio de hombres son:{phom}")
print(f"el promedio de las mujeres  son :{pmu}")

'''Realizar un algoritmo que calcule la edad de una persona.'''
fnac=int(input("ingrese fecha de su nacimiento"))
fact=int(input("ingrese fecha actual"))
edad=fnac -fact
print(f"su edad como tal es {edad}")

#problemas propuestos

'''Dada un cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad
cambiaría es un dato desconocido.'''
masa=str(input("ingrese la cantidad de  masa "))
presion=int(input("ingrese la presion"))
volumen=int(input("ingrese el volumen de la masa"))
temperatura=float(input("ingrese la temperatura de la masa"))
masa=(presion*volumen)/(0.37*(temperatura + 460))

print(f"el resultado de la masa es :{masa}")

'''Leer un numero y escribir el valor absoluto del mismo.'''
num1=int(input("ingrese el numero"))
valor_abs=num1/num1
print(f"el valor absoluto del numero es:{num1}")

'''Calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de
ejercicio, si la formula es:'''

num_pulsaciones=int(input("ingrese numero de pulsaciones"))
edad=int(input("ingrese edad"))
num_pulsaciones=(220-edad)/100
print(f"la cantidad de pulsaciones por minutos son :{num_pulsaciones}")

'''Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario
anterior.'''
sb=float(input("ingrese el salario base"))
valo_horas=int(input("ingrese el valor de las horas"))
horas_tra=int(input("ingrese las horas que trabajo"))
sb=valo_horas+horas_tra
sf=sb*0.25
print(f"el salario final de obrero es :{sf}")

'''En un hospital existen tres áreas: Ginecología, Pediatría, Traumatologia. El presupuesto
anual del hospital se reparte conforme a la sig. tabla: '''
area=str(input("ingrese el numero del area 1-pediatra,2-traumatologia,3-ginecologica"))
if area==1:
    print("su descuento sera del :40%")
elif area==2:
    print("su descuento sera del  40:")
elif area==3:
    print("su area es la 3 y su /n descuento es del :30")

porcentaje=area/100
print(f"la cantidad de dinero a pagar es {porcentaje}")

'''Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas
invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con
respecto a la cantidad total invertida.'''
capital1=str(input("ingrese su capital invertido"))
capital2=str(input("ingrese su capital invertido"))
capital3=str(input("ingrese su capital invertido"))
porcentaje=(int)(capital1+capital2+capital3)/100
print(f"el capital invertido de cada  persona es del:{porcentaje}")

''' '''
cat_pesos=str(input("ingrese la cantidad de pesos"))
cat_dolar=int(input("ingrese la cantidad en dolar"))
cat_pesos,cat_dolar=cat_dolar,cat_pesos
print(f"la cantidad es :{cat_pesos}")
print(f"la cantidad es :{cat_dolar}")

precio_inicial=int(input("ingresio el precio inicial"))
gan=precio_inicial/100
''' Un alumno desea saber cual será su promedio general en las tres materias mas difíciles
que cursa y cual será el promedio que obtendrá en cada una de ellas. Estas materias se
evalúan como se muestra a continuación: '''

matematicas=float(input("digite la calificacion de matematicas:"))
tarea1=float(input("digite nota 1"))
tarea2=float(input("digite nota 1"))
tarea3=float(input("digite nota 1"))
promtarea= tarea1+tarea2+tarea3 /3
examen= matematicas*0.9

fisica=float(input("digite la calificacion de ffisica:"))
tarea1=float(input("digite nota 1"))
tarea2=float(input("digite nota 1"))
promtarea= tarea1+tarea2+tarea3 /2
examen= matematicas*0.8

quimica=float(input("digite la calificacion de ffisica:"))
tarea1=float(input("digite nota 1"))
tarea2=float(input("digite nota 1"))
tarea3=float(input("digite nota 1"))
promtarea= tarea1+tarea2+tarea3 /3
examen= quimica*0.85














