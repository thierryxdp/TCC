def conta_numero(numero,matriz):
    '''função que dado um número e uma matriz retorna quantas vezes esse numero apareceu na matriz:int,list->int'''
    n = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == n:
                n=n+1
    total = matriz.count(n)
    return total