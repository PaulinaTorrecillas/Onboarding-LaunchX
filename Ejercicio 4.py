from matplotlib.pyplot import title


text = "Interesting facts about the Moon.The Moon is Earth's only satellite.There are several interesting facts about the Moon and how it affects life here on Earth.On average,  the Moon moves 4cm away from the Earth every year.This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight"

#Primero, divide el texto en cada oración para trabajar con su contenido:

# Añade el código necesario
text_parts = text.split('.')
text_parts
print(text_parts)

#Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.

# Define las palabras pista: average, temperature y distance suenan bien

key_words = ["average", "temperature", "distance"]
print(key_words)

#Cre un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:

# Ciclo for para recorrer la cadena
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence)
            break
#Finalmente, actualiza el bucle(ciclo) para cambiar C a Celsius:

# Ciclo para cambiar C a Celsius
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence.replace('c', ' Celsius'))
            break

#-------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 2 Formateando Cadenas

# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

#Primero, crea un título para el texto. Debido a que este texto trata sobre la gravedad en la Tierra y la Luna, úsalo para crear un título significativo. Utiliza las variables en lugar de escribir.

# Creamos el título

title=( f'El nombre del planeta es: {planet}')
print(title)

#Ahora crea una plantilla de cadena multilínea para contener el resto de la información.
# En lugar de usar kilómetros, debes convertir la distancia a metros multiplicando por 1,000.

# Creamos la plantilla
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

hechos = f"""{'-'*100} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""
print(hechos)


new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))

# Pista: print(nueva_plantilla.format(variables))
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))


























