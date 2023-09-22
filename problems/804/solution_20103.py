def filtra_pares(numeros):
    """
    Função que recebe quatro números, filtra os que são pares e adiciona os pares em uma
    nova tupla.
    """

    def filtra_pares(x):
    a,b,c,d = x
    pares=tuple()
    
    if a%2==0:
       pares +=(a,)
    if b%2==0:
       pares +=(b,)
    if c%2==0:
       pares +=(c,)
    if d%2==0:
       pares +=(d,)
    return pares