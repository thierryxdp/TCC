# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (A, B, C, H, L):
    """Dadas as dimenssões da porta de altura H e largura L e as dimenssões do colchão A x B x C, calcula e retorna True se o colchão passa pela porta e False se o colchão não passar pela porta. int, int, int, int, int -> bool"""
    dimenssoes = [A, B, C]
    import math
    if max (dimenssoes) < H:
        mensagem = True
    else:
        mensagem = False
    return mensagem