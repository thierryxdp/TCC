def colchao_passa(dimensoes_colchao: list, h: int, l:int) -> bool:
    """Determina se o colchão de dimensões descritas na lista 'dimensoes_colchao'
       passa nas portas de dimensões h (altura) e l (largura)"""

    porta_maior_dim = max(h, l)
    porta_menor_dim = min(h, l)
    passa = True

    if (porta_maior_dim < dimensoes_colchao[1] or
        porta_menor_dim < dimensoes_colchao[0]):
        passa = False
    
    return passa