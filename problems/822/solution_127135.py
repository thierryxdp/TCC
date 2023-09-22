def repetidos(numeros):
    """dada uma lista numeros de entrada, retorna quantas vezes um elemento
    é igual ao anteriror
    list --> int"""
    contador=0
    repeticoes=0
    while contador < len(numeros):
        if numeros[contador]==numeros[contador-1]:
            repeticoes=repeticoes+1
        contador=contador+1
    return repeticoes