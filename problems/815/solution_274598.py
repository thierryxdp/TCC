def insere(lista_numero,n):
    '''
    '''
    lista2= lista_numero + [n]
    list.sort(lista2)
    
    posicao= list.index(lista2,n)
    
    return lista2[posicao+1:]