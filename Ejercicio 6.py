
# Creamos la lista planets y la mostramos
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('Estos son los', len(planets), 'planets')

# Agregamos a plutón y mostramos el último elemento

planets.append('Pluto')

print(planets[-1], 'es el ultimo planeta')

#------------------------------------------------------------------------------------------------------

#EJERCICIO 2 Trabajando con datos de una lista

# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

# Solicitamos el nombre de un planeta *Pista:  input()*
planeta=input("Nombre de un planeta: ")

# Busca el planeta en la lista
planeta_index = planets.index(planeta)

# Muestra los planetas más cercanos al sol
print('Los planetas mas cercanos al sol que: ' + planeta)
print(planets[0:planeta_index])

# Muestra los planetas más lejanos al sol

print('Los planetas mas lejanos del sol que:' + planeta)
print(planets[planeta_index + 1:])