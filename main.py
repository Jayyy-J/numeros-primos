# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Raíz cuadrada para optimizar
        if n % i == 0:
            return False
    return True

# Función para determinar si un número es palindrómico
def es_palindromo(n):
    n_str = str(n)  # Convertimos el número a string
    return n_str == n_str[::-1]  # Verificamos si el número leído al revés es igual

# Función para generar una lista de números primos en un rango dado
def generar_primos(limite):
    primos = []
    for n in range(2, limite + 1):
        if es_primo(n):
            primos.append(n)  # Agregar a la lista si es primo
    return primos

# Función para recorrer la lista de primos e imprimir si 'n' es palindrómico
def verificar_palindromos_en_lista(limite):
    primos = generar_primos(limite)  # Generamos la lista de primos
    print("Verificación de números primos palindrómicos:")
    for i in range(len(primos)):  # Recorremos la lista usando índices
        n = primos[i]  # Número actual en la lista
        if es_palindromo(n):  # Verificar si el número actual es palindrómico
            print(f"{n} es palindrómico")
        else:
            print(f"{n} no es palindrómico")


limite = int(input("Ingresa el límite superior del rango: "))
verificar_palindromos_en_lista(limite)
