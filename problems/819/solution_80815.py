def filtraMultiplos(lista,n):
    '''
       função que recebe lista de numeros e um numero e
       retorna outra lista contendo todos os elementos da
       lista original que forem divisiveis por n 
       list, int -> list
    '''
    i = 0
    divisiveis = []
    while i < len(lista):
        if lista[i] %n == 0:
            divisiveis.append(lista[i])
        i=i+1
    return divisiveis