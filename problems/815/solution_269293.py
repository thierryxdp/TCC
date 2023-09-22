def insere(lista_numero, n):
    '''função que recebe uma lista e um numero e o coloca na 
    lista de tal forma que a mesma continue ordenada de forma crescente'''
    lista_numero.append(n)
    lista=list.sort(lista_numero)
    return lista