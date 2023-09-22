def filtra_pares(a,b,c,d):
    """Entre com 4 números inteiros quaisquer
    para que a função retorne os números pares
    na ordem em que foram passados.
    tupla(int, int, int, int)->tupla"""
    x=[a,b,c,d]
    y=tuple(filter(lambda n: n%2==0, x))
    return y