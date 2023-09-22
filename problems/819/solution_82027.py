def filtraMultiplos(x,n):
    """
    Calcula os numeros divisiveis por n na lista x e retorna outra lista
    contendo os elementos da lista original divisiveis por n;
    list, float -> list
    """
    div = []
    proximo = 0
    while proximo < len(x):
        if x[proximo]%n == 0:
            div = div + [x[proximo],]
        proximo = proximo + 1
    return div