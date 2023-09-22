# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(dimcolchao: list, h: int, l:int) -> bool:
    """Determina se o colchão de dimensões descritas na lista 'dimensoes_colchao'
       passa nas portas de dimensões h (altura) e l (largura)"""

    maior_dim = max(h, l)
    menor_dim = min(h, l)
    passa = True

    if (maior_dim < dimcolchao[1] or
        menor_dim < dimcolchao[0]):
        passa = False
    
    return passa