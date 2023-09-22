def insere(lista_numero, n):
    '''Give an ordered list with intergers, from the smaller to the bigger number,
    and a ramdom number (n) as parameters, respectively. This function
    will put 'n' in the ordered list, without messing with it´s organization.
    list, int --> list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    newList = lista_numero
    return newList