def filtraMultiplos(lista,n):
    ''' funç˜ao que recebe como entrada uma
        lista de números e um número n, e retornar outra lista
        contendo todos os elementos da lista original que
        forem divisíveis por n.
        lista,int->lista'''
    lista1=[]
    indice=0
    tamanhototal=len(lista)
    while indice<tamanhototal:
        if lista[indice]%n==0:
            list.append(lista1,lista[indice])
            indice=indice+1
    return lista1