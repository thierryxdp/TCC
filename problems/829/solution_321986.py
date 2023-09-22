def soma_h(n:int)->float:
    """Determina a soma da série harmônica até o valor da entrada,
    com aproximação de duas casas decimais"""
    valor_soma = sum(map(lambda x: 1/x, range(1,n+1)))
    return round(valor_soma,2)