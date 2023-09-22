def filtraMultiplos(lista,numero):
    '''retorna uma lista contendo todos os elementos da lista original que forem divisiveis por numero. lista,int->lista'''
    i=0
    lista1=[]
    while i<len(lista):
        if lista[i]%numero==0:
            lista1=lista1+lista[i]
        i=i+1
    return lista1