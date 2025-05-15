'''funciones_intermedias_1.py
Ejercicios de funciones intermedias (Core)
Objetivos:
- Practicar iteración de diccionarios y creación de funciones
- Recorrer diccionarios de listas y listas de diccionarios

1. Actualizar valores en diccionarios y listas
2. Iterar a través de una lista de diccionarios
3. Obtener valores de una lista de diccionarios
4. Iterar a través de un diccionario con valores de lista
'''

def actualizar_estructuras():
    # 1. Actualizar valores en diccionarios y listas
    matriz = [[10, 15, 20], [3, 7, 14]]
    matriz[1][0] = 6  # cambia 3 por 6

    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"}
    ]
    cantantes[0]["nombre"] = "Enrique Martin Morales"  # actualiza nombre

    ciudades = {
        "México": ["Ciudad de México", "Guadalajara", "Cancún"],
        "Chile": ["Santiago", "Concepción", "Viña del Mar"]
    }
    # reemplaza "Cancún" por "Monterrey"
    idx = ciudades["México"].index("Cancún")
    ciudades["México"][idx] = "Monterrey"

    coordenadas = [
        {"latitud": 8.2588997, "longitud": -84.9399704}
    ]
    coordenadas[0]["latitud"] = 9.9355431  # actualiza latitud

    # Mostrar resultados
    print("Matriz actualizada:", matriz)
    print("Cantantes actualizados:", cantantes)
    print("Ciudades actualizadas:", ciudades)
    print("Coordenadas actualizadas:", coordenadas)


def iterarDiccionario(lista):
    '''Recorre una lista de diccionarios e imprime sus llaves y valores.'''
    for dic in lista:
        pares = [f"{k} - {dic[k]}" for k in dic]
        print(', '.join(pares))


def iterarDiccionario2(llave, lista):
    '''Imprime el valor de una llave específica en cada diccionario de la lista.'''
    for dic in lista:
        if llave in dic:
            print(dic[llave])
        else:
            print(f"La llave '{llave}' no existe en {dic}")


def imprimirInformacion(diccionario):
    '''Imprime el nombre de cada clave, la cantidad de elementos y los valores.'''
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for v in valores:
            print(v)
        print()  # línea en blanco entre secciones


if __name__ == "__main__":
    # Parte 1
    actualizar_estructuras()

    print("\n--- Iterar diccionario de cantantes ---")
    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"},
        {"nombre": "José José", "pais": "México"},
        {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
    ]
    iterarDiccionario(cantantes)

    print("\n--- IterarDiccionario2 (nombre) ---")
    iterarDiccionario2("nombre", cantantes)

    print("\n--- Imprimir información de costa_rica ---")
    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }
    imprimirInformacion(costa_rica)
