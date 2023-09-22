def filtraMultiplos(numeros,n):
    """ Função que recebe como entrada uma lista de números e
        um número n, e retorna uma outra lista contendo todos
        os elementos da lista original que forem divisíveis 
        por n;
        list(float), float -> list(float)"""
    i = 0 #representa os índices dos elementos da lista de números
    multiplos = [] #armazena os números múltiplos de n 
    while i<len(numeros):
        if numeros[i]%n == 0:
            multiplos = multiplos + [numeros[i]]
        i = i+1
    return multiplos