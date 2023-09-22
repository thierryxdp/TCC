def soma_h(n):
    """Para calcular e retornar o valor de H com N termos inteiros, digite
    int->float"""
    h=0
    for i in range(1,n+1):
        h+= 1/i
    return round (h,2)