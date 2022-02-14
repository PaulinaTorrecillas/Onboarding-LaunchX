#Ejercicio 1: Creación de un bucle "while"
#Ejercicio 1: Uso de ciclos while en Python
#En Python, los ciclos while te permiten ejecutar código un número desconocido de veces. 
# Los ciclos examinan una condición booleana y, siempre que la condición sea verdadera, se ejecutará el código dentro del ciclo. 
# Esto es muy útil para situaciones como solicitar valores a un usuario.
#En este ejercicio, estás creando una aplicación que solicita a un usuario que ingrese una lista de planetas. En un ejercicio posterior, agregarás código que muestre la lista. Por ahora,
# crearás solo el código que solicita al usuario la lista de planetas.

# Declara dos variables
new_planet=""
planets=[]
# Escribe el ciclo while solicitado
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet ')

#------------------------------------------------------------------------------------------------------
#Ejercicio 2: Creación de un ciclo "for"

#Ejercicio: - Ciclo para una lista
#En el ejercicio anterior, creaste código para solicitar a los usuarios que introduzcan una lista de nombres de planetas.
#  En este ejercicio, completarás la aplicación escribiendo código que muestre los nombres de esos planetas.
#Mostrar la lista de los planetas
#La variable planets almacena los nombres de planeta que ha introducido un usuario. Ahora usarás un ciclo para mostrar esas entradas.
#Crea un ciclo for para iterar sobre la lista planets. Puedes usar como nombre de la variable planet para cada planeta. 
# Dentro del ciclo for, recuerda utilizar print para mostrar cada planet.

# Escribe tu ciclo for para iterar en una lista de planetas

for planet in planets:
    print(planet)


