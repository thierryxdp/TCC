def insere(lista_numero,n):
    """ Função que insere o número n na posição correta para que a lista fique em ordem crescente
    list,int -> list """
    lista_numero=list.append(lista_numero,n)
    lista_numero=list.sort(lista_numero)
    return lista_numero