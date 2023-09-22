def insere(lista_numero,n):
    '''adiciona um numero a uma lista de numeros de forma ordenada'''
    lista=lista_numero+[n]
    resultado=sorted(lista)
    return resultado