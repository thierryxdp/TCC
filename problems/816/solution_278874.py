def maiores(lista,n):
    """A função retorna os números maiores que n na lista dada.
    list, int - > list"""
    lista.append(n)
    lista.sort()
    indice=lista.index(n)
    resposta= lista[n:]
    return resposta