def soma_h(n):
    """Calcula e retorna o valor H com n termos;
       int->float
       Parametro:
       n: numero inteiro qualquer
    """
    H=1
    for num in range(2,n+1):
        div=1/num
        H+=div
    return round(H,2)