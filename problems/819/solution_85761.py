def filtraMultiplos (lista,n):
    '''função que filtra os múltiplos de um número n, recebe como entrada uma lista de numeros e o número e retorna uma outra lista contendo todos os elementos da lista original que forem divisíveis por n. list, float-> list'''
    lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i])%n == 0:
            lista1 = lista1 + (lista[i],)
            i = i+1
            return list(lista1)