# Equipo 4
# Jennyfer Nahomi Jasso Hernández A01749898
# Emiliano Caballero Mendoza A01749050

# Codigo 1
#ENTRADAS
numero=int(input("Dame un numero del 1 al 7: "))
#PROCESAMIENTO/SALIDAS
if(numero==1):
  print("Lunes")
elif(numero==2):
  print("Martes")
elif(numero==3):
  print("Miercoles")
elif(numero==4):
  print("Jueves")
elif(numero==5):
  print("Viernes")
elif(numero==6):
  print("Sabado")
elif(numero==7):
  print("Domingo")
else:
  print("ERROR")
  
#Codigo 2
#ENTRADAS
num1=int(input("Dame el primer numero: "))
num2=int(input("Dame el segundo numero: "))
num3=int(input("Dame el tercer numero: "))
#PROCESAMIENTO/SALIDAS
if((num1+num2==num3) or (num2+num3==num1) or (num3+num1==num2)):
  print("True")
else:
  print("False")

#Codigo 3
#ENTRADAS
dinero=int(input("¿Cuánto tienes en el banco? "))
interes=int(input("¿Cuál es la tasa de interés mensual? "))
#PROCESAMIENTO
interesTotal=(dinero*interes)/100
reinversion=dinero+interesTotal
#SALIDAS 
if(interesTotal>=7000):
  print(f"${reinversion:,.2f}")
else:
  print("No hubo reinversión")
  
#Codigo 4
#ENTRADAS
num1=int(input("Dame el primer número: "))
num2=int(input("Dame el segundo número: "))
num3=int(input("Dame el tercer número: "))
#PROCESAMIENTO
if((num1<=num2) and (num1<=num3)):
    menor=num1
    if(num2<=num3):
        medio=num2
        mayor=num3
    else:
        medio=num3
        mayor=num2

elif((num2<=num1) and (num2<=num3)):
    menor=num2
    if(num1<=num3):
        medio=num1
        mayor=num3
    else:
        medio=num3
        mayor=num1

elif((num3<=num1) and (num3<=num2)):
    menor=num3
    if(num1<=num2):
        medio=num1
        mayor=num2
    else:
        medio=num2
        mayor=num1
#SALIDAS
print(menor)
print(medio)
print(mayor)

#Codigo 5
#ENTRADAS
actividad=str(input("¿Qué actividad realiza? "))
tiempo=int(input("¿Durante cuántos minutos? "))
act1="dormir"
act2="sentar"
dormir=1.08
sentado=1.66
#PROCESAMIENTO
calSent=sentado*tiempo
calDorm=dormir*tiempo
#SALIDAS
if(actividad==act1):
  print(f"Consumiste {calDorm:,.2f} calorías")
elif(actividad==act2):
  print(f"Consumiste {calSent:,.2f} calorías")

#Codigo 6
#ENTRADAS
num1=int(input("Dame el primer número: "))
num2=int(input("Dame el segundo número: "))
#PROCESAMIENTO
mult=num1*num2
resta=num1-num2
suma=num1+num2
#SALIDAS
if(num1==num2):
  print(mult)
elif(num1>num2):
  print(resta)
else:
  print(suma)
  
#Codigo 7
#ENTRADAS
salarioActual=int(input("¿Cuál es tu salario mensual? "))
años=float(input("Dame la antigüedad en años: "))
#PROCESAMIENTO
menos1=salarioActual*.05
mas1menos2=salarioActual*.07
mas2menos5=salarioActual*.1
mas5menos10=salarioActual*.15
mas10=salarioActual*.2
#SALIDAS
if(años<1):
  print(f"${menos1:,.2f}")
elif(1<=años<2):
  print(f"${mas1menos2:,.2f}")
elif(2<=años<5):
  print(f"${mas2menos5:,.2f}")
elif(5<=años<10):
  print(f"${mas5menos10:,.2f}")
else:
  print(f"${mas10:,.2f}")
  
#Codigo 8
#ENTRADAS
edad=int(input("Dime tu edad: "))
antigüedad=int(input("Dime tu antigüedad: "))
#PROCESAMIENTO/SALIDAS
if((edad>=60) and (antigüedad<25)):
  print("por edad")
elif((edad<=60) and (antigüedad>=25)):
  print("por antigüedad joven")
elif((edad>=60) and (antigüedad>=25)):
  print("por antigüedad adulta")
else:
  print("no aplica")
  
#Codigo 9
#ENTRADAS
num = int(input("cuantas computadoras compro: "))

precio = 11000
# PROCESAMIENTO
precioTotal = num * precio

des1 = 0.10 * precioTotal
des2 = 0.20 * precioTotal
des3 = 0.40 * precioTotal

total1 = precioTotal - des1
total2 = precioTotal - des2
total3 = precioTotal - des3

# SALIDAS
if(0 < num < 5):
    print(f"Su descuento es de: ${des1}")
    print(f"Su total es de: ${total1}")
elif(10 > num >= 5):
    print(f"Su descuento es de: ${des2}")
    print(f"Su total es de: ${total2}")
else:
    print(f"Su descuento es de: ${des3}")
    print(f"Su total es de: ${total3}")
    
#Codigo 10
#ENTRADAS
respuesta = input("¿Colón descubrió América? ")
#PROCESAMIENTO Y SALIDAS
if(respuesta == "si"):
    respuesta = input("¿La independencia fue en 1810? ")
    if(respuesta == "si"):
        respuesta = input("¿The Doors fue un grupo de rock Americano? ")
        if(respuesta == "si"):
            print("FELICIDADES, GANASTE")
        else:
            print("PERDISTE")    
    else:
        print("PERDISTE")
else:
    print("PERDISTE")