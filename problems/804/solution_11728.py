def filtra_pares(a,b,c,d):
    """Função que dado uma tupla com quatro parâmetros, retornará apenas os pares na mesma ordem original."""
    tupla1=[]
    if a%2==0:
        return [a,]
    elif b%2==0:
        return tupla1+[b,]
    elif c%2==0:
        return [c,]+tupla1
    elif d%2==0:
        return [d,]+tupla1