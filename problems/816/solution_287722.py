def maiores(lista_numero,n):
    '''retorna n na colocação correta de uma lista crescente dada
    list,int->list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero