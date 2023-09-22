def insere(lista_numero,n):
    '''insere o número n na lista de modo que n esteja em uma posição
    ordenada na lista
    list,int->list'''
    
    lista=lista_numero
    list.insert(lista,0,n)
    list.sort(lista)
    
    return lista