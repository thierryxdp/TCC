def insere(lista_numero, n):
    '''insere n na posição correta em uma lista ordenada'''
    ordenada = lista_numero.append(n)
    ordenada = list.sort(lista_numero)
    return ordenada