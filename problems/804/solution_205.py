def filtra_pares(a,b,c,d):
    """Entre com 4 números inteiros quaisquer
    para que a função retorne os números pares
    na ordem em que foram passados.
    tupla(int, int, int, int)->tupla"""
    x=(a,b,c,d)
    pares=()
    for n in range(4):
        if x[n]%2==0:
            pares=pares+(x[n],)
    return pares