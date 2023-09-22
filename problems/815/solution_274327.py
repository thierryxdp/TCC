def insere(lista_numero,n):
    '''Retorna a lista com o n na posição correta ordenada.'''
    lista_numero.insert(lista_numero, n)
    list.sort(lista_numero)
    
    return lista_numero