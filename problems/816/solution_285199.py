def maiores(lista,n):
    '''funcao que recebe uma lista e o numero n
    	e retorna uma nova lista com todos os numeros maiores que n
        n: int
        return: int
    '''
    list(lista)
    lista.append(n)
    listaO = sorted(lista)
    indice = listaO.index(n)
    if n not in listaO:
        lista.append(n)
    return listaO[indice + 1:]