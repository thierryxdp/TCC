def insere(lista,n):
    '''...lista,int->'''
    indice = lista[len(lista):len(lista)]
    
    list.insert(lista,indice,n)
    
    return list.sort(lista)