def filtraMultiplos(numeros,n):
    '''Função que recebe como entrada uma lista de números e um número, e retorns outra lista contendo todos os elementos da lista original que forem divisíveis por n; list, int -> list'''
    multiplos = []
    i = 0
    while i<len(numeros):
        if numeros[i]%n ==0:
            multiplos = multiplos+numeros[i]
        i=i+1
     return multiplos