def soma_h(n:int)->float:
    valor_soma = sum(map(lambda x: 1/x, range(1,n+1)))
    return round(valor_soma,2)