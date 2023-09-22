def filtra_pares(t):
    """Recebe uma tupla com quatro inteiros como parâmetro
    Retorna uma tupla contendo apenas os números pares
    tuple->tuple"""
    [a,b,c,d]=t
    if a%2=0 and b%2=0 and c%2=0 and d%=0:
        return(a,b,c,d)
    elif a%2=0 and b%2=0 and c%2=0 and d%!=0:
        return (a,b,c)
    elif a%2=0 and b%2=0 and c%2!=0 and d%!=0:
        return(a,b)
    elif a%2=0 and b%2!=0 and c%2!=0 and d%!=0:
        return (a)
    else:
        return()