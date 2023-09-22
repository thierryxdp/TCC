def filtra_pares(a,b,c,d):
    """Função que recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original;tuple->tuple"""
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return(a,b,c,d)
    if a%2==0 and b%==0 and c%2==0:
        return (a,b,c)
    if a%2==0 and b%==0 and d%2==0:
        return (a,b,d)
    if a%2==0 and c%==0 and d%2==0:
        return (a,c,d)
    if b%2==0 and c%==0 and d%2==0:
        return (b,c,d)
    if a%2==0 and b%==0:
        return (a,b)
    if a%2==0 and b%==0: 
        return (a,b)
    if a%2==0 and c%==0: 
        return (a,c)
    if a%2==0 and d%==0: 
        return (a,d)
    if b%2==0 and c%==0: 
        return (b,c)
    if b%2==0 and d%==0: 
        return (b,d)
    if c%2==0 and d%==0:
        return (c,d)
    if a%2==0:
        return(a,)
    if b%2==0:
        return(b,)
    if c%2==0:
        return(c,)
    if d%2==0:
        return(d,)