def maiores(lista_numero,n):
    '''retorna n na colocação correta de uma lista crescente dada
    list,int->list'''
    lista_numero.append(n)
    Lista=lista_numero.sort().reverse
    
    if Lista is True:
        return list.sort(lista_numero)
    elif Lista is False:
        return list.sort(lista_numero)