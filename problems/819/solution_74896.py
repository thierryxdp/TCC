def filtraMultiplos(lista,n):
    ''' função que recebe como entrada uma
        lista de números e um número n, e retornar outra lista
        contendo todos os elementos da lista original que
        forem divisíveis por n.
        lista,int->lista'''
    lista1=[]
    i=0
    tamanhofinal=len(lista)
    while i<tamanhofinal:
        if lista[i]%n==0:
            i=i+1
            continue
        lista1.append(lista[i])
        i=i+1
    return lista1