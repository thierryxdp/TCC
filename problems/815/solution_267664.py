def insere(lista_numero,n):
    """funcao que retorna uma lista ordenada com o acrescimo do numero n
    list,int -> list"""

    lista_nova = lista_numero.append(n)
    lista_nova = lista_nova.sort()
    return lista_nova