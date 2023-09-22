def qtd_divisores(n):
    """Retorna quantos divisores o número(n) tem.
    int/float->int"""
    div=0
    for c in range(1,n+1):
        if n%c==0:
            div+=1
    return div