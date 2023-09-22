def primo (n):
    """..."""
    
    lista_numeros = list(range(2,n))
    contador_divisores = 0

    for numero in lista_numeros:
        if n % numero == 0:
            contador_divisores = contador_divisores + 1
    if contador_divisores == 0:
        return True
    else:
        return False