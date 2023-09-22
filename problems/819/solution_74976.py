def filtraMultiplos(lista,n):
    ''' função que recebe como entrada uma
        lista de números e um número n, e retorna outra lista
        contendo todos os elementos da lista original que
        forem divisíveis por n.
        lista,int->lista'''
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            list.append(lista1,lista[i])
        i=i+1
    return lista1