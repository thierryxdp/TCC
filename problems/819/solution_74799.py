def filtraMultiplos(listaNum, n):
    '''Recebe uma lista de números e um número 'n' e retorna outra lista
    que contém todos os elementos da lista original que são divisíveis
    por 'n'.
    
    list, float -> list'''

    contador = 0
    multiplos_n = []

    while contador < len(listaNum):
        if listaNum[contador]%n == 0:
            multiplos_n = multiplos_n + [listaNum[contador]]
        contador = contador + 1
    return multiplos_n