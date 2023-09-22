def posLetra(string,letra,n):
    posicao = 0
    lista = []
    
    if n > str.count(string, letra):
        return -1
    
    while posicao < len(string):
        if string[posicao] == letra:
            list.append (lista,posicao)
        posicao = posicao + 1
    return lista[n-1]