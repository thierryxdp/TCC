def filtraMultiplos(lista,n):
    ''' funç˜ao que recebe como entrada uma
        lista de números e um número n, e retorna outra lista
        contendo todos os elementos da lista original que
        forem divisíveis por n.
        lista,int->lista'''
    lista1=[]
    i=0
    tamanhofinal=len(lista)
    while i<tamanhofinal:
        if lista[i]%n==0:
            lista1=list.append(lista1,lista[i])
        i=i+1
    return lista1