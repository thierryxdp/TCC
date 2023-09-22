def maiores(lista,n):
    '''Retorna uma nova lista que contém todos os números da lista
    original maiores que n e ordenados de forma crescente
    list,int->list'''
    
    list.insert(lista,0,n)
    list.sort(lista)
    indice=list.index(lista,n)+1
    totalelementos=len(lista)
    novalista=lista[indice:totalelementos]
    return novalista

def acima_da_media(lista):
    '''Retorna uma lista ordenada com as notas que
    ficaram acima da média
    list->list'''
    
    media=sum(lista)/len(lista)
    list.insert(lista,0,media)
    list.sort(lista)
    indice=list.index(lista,media)
    list.del(lista,indice)
    totalelementos=len(lista)
    return lista[indice:totalelementos]