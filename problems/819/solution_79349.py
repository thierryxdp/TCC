def filtraMultiplos(lista_numeros,n):
    """ Função que recebe como entrada uma lista de números e
        um número n, e retorna uma outra lista contendo todos
        os elementos da lista original que forem divisíveis 
        por n;
        list(int), int -> list(int)"""
    i = 0 #representa os índices dos elementos da lista de números
    multiplos = [] #armazena os números múltiplos de n 
    while i<len(numeros):
        if lista_numeros[i]%n == 0:
            multiplos = multiplos + [lista_numeros[i]]
        i = i+1
    return multiplos