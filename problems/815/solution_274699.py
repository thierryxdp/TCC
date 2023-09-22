def insere(lista_numero,n):
    '''recebe uma lista ordenada de forma crescente e devolver
    essa lista com a inclusão do numero n na posição n de forma q ainda
    seja crescente'''
    lista2= list.insert(lista_numero, n, n)
    return list.sort(lista2)