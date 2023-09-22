def qtd_divisores(n):
    """..."""
    
    lista_numeros1aN = list(range(1,n+1))
    contador_divisores = 0

    for numero in lista_numeros1aN:
        if n % numero == 0:
            contador_divisores = contador_divisores + 1
    return contador_divisores