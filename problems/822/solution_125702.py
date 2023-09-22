def repetidos(numeros):
    """Retorna quantas vezes um elemento da lista e igual
    	ao elemento anterior.
        list-->int"""
    proximo = 0
    n = 0
    while proximo < len(lista):
        if numeros[proximo]==numeros[proximo-1]:
            n = n+1
        proximo = proximo+1
    return n