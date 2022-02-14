#Para este ejercicio, escribirás una lógica condicional que imprima una advertencia 
# si un asteroide se acerca a la Tierra demasiado rápido. 
# La velocidad del asteroide varía dependiendo de lo cerca que esté del sol, 
# y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.

#Un asteroide se acerca, y viaja a una velocidad de 49 km/s.

# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
aster=49
if aster > 25:
    print("Cuidado un asteroide esta cerca de la tierra")
else:
    print("Todo esta en orden")

#Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s,
#  a veces produce un rayo de luz que se puede ver desde la Tierra. Escribe la lógica condicional 
# que usa declaraciones if, else, y elif para alertar a las personas de todo el mundo 
# que deben buscar un asteroide en el cielo. 
# ¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

asteroide=19
if asteroide >20:
    print(" Mira ay un rayo de luz")
elif asteroide ==20:
    print(" Mira ay un rayo de luz")
else:
    print("No hay ninguna luz")

#En este ejercicio, aprenderás información más matizada sobre cuándo los asteroides representan un peligro para la Tierra, 
# y utilizarás esa información para mejorar nuestro sistema de advertencia. Aquí está la nueva información que necesitas saber:
#*Los asteroides de menos de 25 metros en su dimensión más grande probablemente se quemarán a medida que entren en la atmósfera de la Tierra.
#Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros golpeara la Tierra, causaría mucho daño.
#También discutimos en el ejercicio anterior que:
#La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.
#Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra.
#Usando toda esta información, escribe un programa que emita la advertencia o información correcta a la gente de la Tierra, según la velocidad y el tamaño de un asteroide. 
# Utiliza instrucciones if, else, y elif, así como los operadores and y or.

# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

velocidad_asteroide = 25
tamano_asteroide = 50
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')


