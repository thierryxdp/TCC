def insere(lista_numero,n):
    '''Insere um determinado numero inteiro em uma sequência de modo que 
    a lista continue ordenada
    list, int->lista'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero