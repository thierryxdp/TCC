def filtraMultiplos (listaN,n):
    """ funcao ira receber uma lista de numeros e um numero n, e retornar uma lista contendo todos os numeros
    dessa lista que sejam divisiveis por n
    entrada: lista, int     saida: lista"""
    multiplos = []
    proximo = 0
    while proximo < len(listaN) :
        if listaN [proximo] % n == 0:
            multiplos = multiplos + [listaN[proximo]]
        proximo = proximo + 1 
    return multiplos