def maiores(lista,numero):
    lista_maior=lista
    lista_maior+=[numero]
    lista_maior.sort()
    posicao=lista_maior.index(numero)
    del lista_maior[:posicao+1]
    return lista_maior