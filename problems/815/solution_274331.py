def insere(lista_numero,n):
    '''Retorna a lista com o n na posição correta ordenada.'''
    lista_numero.append(n)
    list.sort(lista_numero)
    
    return lista_numero