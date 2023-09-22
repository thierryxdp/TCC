def filtra_pares(p):
    """Função que recebe uma tupla com quatro elementos inteiros e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original.
    
    tuple -> tuple
    
    Parameters:
    p: tupla com quatro elementos do tipo int"""
    a,b,c,d = p
    s=()
    if a%2==0:
        s=s+(a,)
    if b%2==0:
        s=s+(b,)
    if c%3==0:
        s=s+(c,)
    if d%2==0:
        s=s+(d,)
    return s