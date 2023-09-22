def insere(lista_numero, n):
    '''função que acrescenta n na posição coreta em uma lista ordenada'''
    ordenada = lista_numero.append(n)
    ordenada1 = list.sort(lista_numero)
    return lista_numero