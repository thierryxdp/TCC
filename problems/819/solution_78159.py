def filtraMultiplos (lista,n):
    '''funcao que retorna uma lista contendo todos os
    elementos da lista original que forem divisiveis por n
    list,int->list'''
    listamultiplos=[]
    f=0
    while f<len(lista):
        if lista[f]%n==0:
            listamultiplos=listamultiplos+[lista[f]]
        f=f+1
    return listamultiplos