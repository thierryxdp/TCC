def maiores(lista,n):
    '''dada uma lista e um inteiro n, retorna uma nova lista ordenada com apenas os numeros da lista original que sao maiores que n; list,int -> list'''
    i = 0
    novalista = []
    while i < len(lista):
        if lista[i] > n:
            novalista = novalista + [lista[i],]
        else:
            novalista = novalista
        i = i + 1
    list.sort(novalista)
    return novalista