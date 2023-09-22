def insere(lista,n):
    '''...lista,int->'''
    indice = list.index(lista,n)
    
    list.insert(lista,indice,n)
    
    return list.sort(lista)