# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Raíz cuadrada para optimizar
        if n % i == 0:
            return False
    return True

# Función para generar una lista de números primos en un rango dado
def generar_primos(limite):
    primos = []
    for n in range(2, limite + 1):
        if es_primo(n):
            primos.append(n)  # Agregar a la lista si es primo
    return primos

# Función para imprimir los nodos consecutivos en la lista de primos
def imprimir_nodos_consecutivos(limite):
    primos = generar_primos(limite)  # Generamos la lista de primos
    print("Los nodos de primos consecutivos son:")
    for i in range(len(primos) - 1):  # Recorrer la lista hasta el penúltimo nodo
        n1 = primos[i]
        n1_1 = primos[i + 1]
        print(f"({n1}, {n1_1})")  # Imprimimos el nodo actual y el siguiente

# Programa principal
def main():
    limite = int(input("Ingresa el límite superior del rango: "))
    imprimir_nodos_consecutivos(limite)

# Ejecutar el programa
if __name__ == "__main__":
    main()
