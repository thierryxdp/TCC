def filtraMultiplos(listaN, n):
    """funcao que recebe uma lista de numeros e um numero n e retorna outra lista com todos os elementos da lista original que forem divisiveis por n;
    lista, int->lista"""
    multiplos = []
    proximo = 0
    while proximo < len(listaN) :
        if listaN [proximo] % n == 0:
            multiplos = multiplos + [listaN[proximo]]
            proximo = proximo + 1
            return multiplos