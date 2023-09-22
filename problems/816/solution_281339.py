def maiores(lista,numero):
    lista_menor=lista
    lista_menor+=[numero]
    lista_menor.sort()
    posicao=lista_menor.index(numero)
    del lista_menor[posicao:]
    return lista_menor