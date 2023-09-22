def repetidos(lista):
    """recebe uma lista de numeros, e retorne o numero de vezes que um 
    elemento da lista e igual ao elemento anterior"""
    i = 1
    contador = 0
    while i < len(lista):
        if lista[i-1] == lista [i]:
            contador += 1
        i += 1
    return contador