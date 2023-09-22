def insere(lista,n):
    ''' retorna a lista com o elemento 'n' dentro da lista dada como paramento
        na ordem crescente'''
    lista.append(n)
    lista.sort()
    
    return lista