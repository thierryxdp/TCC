# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (A, B, C, H, L):
    """Dadas as dimenssões da porta de altura H e largura L e as dimenssões do colchão A x B x C, calcula e retorna True se o colchão passa pela porta e False se o colchão não passar pela porta. int, int, int, int, int -> bool"""
    import math
    dimenssoes = []
    if max (A,B,C):
        dimenssoes[0] = max (A,B,C)
    if min (A,B,C):
        dimenssoes[2] = min (A,B,C)
    else:
        dimenssoes[1]