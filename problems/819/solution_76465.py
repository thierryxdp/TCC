def filtraMultiplos(listaNum,n):
    '''Funcao que recebe uma lista de numeros e um numero, retornando
outra lista contendo todos os elementos da original divisores de n'''
    listaDiv = []
    i = 0
    while i < len(listaNum):
        if listaNum[i]%n == 0:
            list.append(listaDiv,listaNum[i])
        i = i+1
    return listaDiv