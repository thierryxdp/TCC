def soma_h(n):
    """Função que retorna soma H
signature: integer --> floating
"""
    lis = []
    for x in range (1, n+1, 1):
        lis = lis + [1/x]
    return round(sum(lis),2)