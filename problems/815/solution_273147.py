def insere(lista_numero, n):
    """função recebe uma lista, adiciona o elemento n à lista e a ordena
    retorna uma lista
    list, int--> list"""

    lista = lista_numero.insert(-1, n)  #insere n na penúltima posição da lista
    list.sort(lista)                   #organiza a lista em ordem crescente
    return lista