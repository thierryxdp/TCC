def filtraMultiplos (lista,n):
    '''função que filtra os múltiplos de um número n, recebe como entrada uma lista de numeros e o número e retorna uma outra lista contendo todos os elementos que forem divisíveis por n. list-> list'''
    multiplos = []
    i = 0
    for i in range(len(lista)):
        if lista [i]%n == 0:
            multiplos.append(lista[i])
            return (multiplos)