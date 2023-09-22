def soma_h(n):
    """A função calcula e retorna o valor da soma de frações
    com N termos; int->float"""
    h=0
    for i in range(1,n+1):
        h = h+(1/i)
    return round(h,2)