def faltante(lista):
    posicao=0
    lista.sort()
    while posicao < len(lista):
        if (lista[posicao] - lista[posicao-1]) > 1:
            return lista[posicao]-1
        posicao = posicao + 1
        if 1 in lista:
            return len(lista) + 1 
        else:
            return 1