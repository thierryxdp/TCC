def insere(lista_numero,n):
    '''função que dada uma lista ordenada de numeros, insere n na posição correta
    str --> str'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero