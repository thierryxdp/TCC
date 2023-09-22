def filtra_pares(a,b,c,d):
    """Função que dado uma tupla com quatro parâmetros, retornará apenas os pares na mesma ordem original."""
    tupla1=[]
    if a%2==0:
        [a,]
    elif b%2==0:
        tupla1+[b,]
    elif c%2==0:
        [c,]+tupla1
    elif d%2==0:
        [d,]+tupla1
    return tupla1