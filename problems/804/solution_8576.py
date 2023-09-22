def filtra_pares(n1,n2,n3,n4):
    """dados 4 numeros inteiros retorna-se os pares em sequencia
    int,int,int,int->int"""
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        return [n1,n2,n3,n4]