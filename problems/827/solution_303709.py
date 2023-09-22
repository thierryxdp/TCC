def qtd_divisores(n):
    """Essa funcao retorna a quantidades de divisores
       que um nuero n tem
       int, -> int"""
    qntDivisores = 0
    for i in range(1,n+1):
        if n%i == 0:
            qntDivisores +=1
    return qntDivisores