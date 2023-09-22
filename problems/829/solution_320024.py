def soma_h(n:int)->float:
    """Dado um valor inteiro n, retorna a soma das iterações 1 sobre 1, somando 1 no denominador até chegar a n."""
    h=0
    for numero in range(1,n+1):
        h=h+(1/numero)
    return round(h,2)