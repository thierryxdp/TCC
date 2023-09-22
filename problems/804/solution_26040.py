def filtra_pares(x):
    """recebe uma tupla(x) com 4 numeros inteiros e 
    retorna os que sao pares. entrada e saida: int"""
    pares=()
    a,b,c,d=x
    if a%2==0: pares=pares+(a,)
    if b%2==0: pares=pares+(b,)
    if c%2==0: pares=pares+(c,)
    if d%2==0: pares=pares+(d,)
    return pares