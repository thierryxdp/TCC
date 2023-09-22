def repetidos(numeros):
    """Retorna quantas vezes um elemento da lista e igual
    	ao elemento anterior.
        list-->int"""
    proximo = 0
    n = 0
    while proximo < len(numeros):
        if numeros[proximo]==numeros[proximo-1]:
            list.append(lista,1)
        proximo = proximo+1
    return sum(lista)