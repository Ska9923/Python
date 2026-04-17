matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 1. Cambiar 3 por 6 en matriz
matriz[1][0] = 6

# 2. Cambiar nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"

# 3. Cambiar "Cancún" por "Monterrey"
ciudades["México"][2] = "Monterrey"

# 4. Cambiar latitud
coordenadas[0]["latitud"] = 9.9355431

# Ver resultados
print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)


#-----------------------------------------------
def iterarDiccionario(lista):
    for dic in lista:
        elementos = []
        for clave, valor in dic.items():
            elementos.append(f"{clave} - {valor}")
        print(", ".join(elementos))


# Ejemplo
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

#-----------------------------------------------------------------
def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])

# Ejemplo
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario2("nombre", cantantes)
print("----")
iterarDiccionario2("pais", cantantes)

#----------------------------------------------------------------------------
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        print()  # línea en blanco para separar

# Ejemplo
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)

