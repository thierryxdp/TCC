def insere(lista,numero):
    lista[0:0] = numero
    lista = list.sort(lista)
    return lista