def filtaMultiplos(lista,n):
    '''receber como entrada uma lista de números e um número, e retornar outra lista contendo todos os elementos da lista original que forem divisíveis por n'''
    i = 0
    mult = []
    while i< len(lista):
        if lista[i]%n==0:
            mult=append(lista[i])
        i= i+1
            return mult