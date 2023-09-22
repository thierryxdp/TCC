def filtra_pares(n1,n2,n3,n4):
    """dados 4 numeros inteiros retorna-se os pares em sequencia
    int,int,int,int->int"""
    return list(range(min(n1,n2,n3,n4),max(n1,n2,n3,n4)+1,2)))