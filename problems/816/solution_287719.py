def maiores(lista_numero,n):
    '''retorna n na colocação correta de uma lista crescente dada
    list,int->list'''
    lista_numero.append(n)
    Lista=lista_numero.sort()
    
    if Lista.reverse is True:
        return list.sort(lista_numero)
    elif Lista.reverse is False:
        return list.sort(lista_numero)