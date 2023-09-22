def insere(lista_numero,n):
    '''Esta função incluiu um numero inteiro numa lista crescente 
    de modo que a lista continua ordenada
    list, int>>>list '''
    
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    
    return lista_numero