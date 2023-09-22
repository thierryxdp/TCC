def filtra_pares(a,b,c,d):
    """Função que dado uma tupla com quatro parâmetros, retornará apenas os pares na mesma ordem original."""
    if a%2==0:
        return [a,]
    elif b%2==0:
        return [a,]+[b,]
    elif c%2==0:
        return [c,]+([a,]+[b,])
    elif d%2==0:
        return [d,]+([a,]+[b,]+[c,])