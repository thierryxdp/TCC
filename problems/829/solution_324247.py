def soma_h(n):
    """recebe um inteiro e retorna a soma dos números inversos de 1 até n
    int->float"""
    h=0
    l=list(range(n+1))
    for x in l[1:]:
        h=h+(1/x)
    return round(h,2)