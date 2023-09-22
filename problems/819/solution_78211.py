def filtraMultiplos (l,n):
    """funcao que recebe uma lista e um numero, e retorna outra lista com todos os numeros divisiveis por n """
    """list, int -> list"""
    listafinal = []
    proximo = 0
    
    while proximo <len(l):
        if l[proximo]%n == 0:
            listafinal = listafinal + [l[proximo],]
        proximo = proximo + 1
    return listafinal