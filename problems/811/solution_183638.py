# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao_passa(dimensoes_colchao: list, h: int, l:int) -> bool:
    """Determina se o colchão de dimensões descritas na lista 'dimensoes_colchao'
       passa nas portas de dimensões h (altura) e l (largura)"""

    maiordim = max(h, l)
    menordim = min(h, l)
    passa = True

    if (maiordim < dimensoes_colchao[1] or
        menordim < dimensoes_colchao[0]):
        passa = False
    
    return passa