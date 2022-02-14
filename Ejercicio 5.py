 #Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!
Tierra =149597870 
Jupiter =778547200

# Calcular la distancia entre planetas
distancia= Jupiter - Tierra
print(distancia)

millas= distancia * 0.621
print(millas)

#----------------------------------------------------------------------------------------------------
#EJERCICIO 2 convierte cadenas en números y usa valores absolutos
# Almacenar las entradas del usuario
#Pista: variable = input("¿Cuál es tu nombre?")
planeta1= input("favor de ingresar el valor de la distancia del primer planeta: " )
planeta2= input("favor de ingresar el valor de la distancia del Segundo planeta: " )

# Convierte las cadenas de ambos planetas a números enteros
planeta1=int(planeta1)
planeta2=int(planeta2)

# Realizar el cálculo y determinar el valor absoluto
distancia = planeta2 - planeta1
print(distancia)

# Convertir de KM a Millas
millas = distancia* 0.621
print(abs(millas))

