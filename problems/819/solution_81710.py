def filtraMultiplos(lista,n):
    """ Função que dada uma lista e um número n, retorna outra lista contendo todos os elementos da lista original que forem divisíveis pelo número n
    list,int -> list """
    i=0
    listafinal=[]
    while i<len(lista):
        if lista[i]%n==0:
            listafinal=listafinal+[lista[i]]
        i=i+1
    return listafinal