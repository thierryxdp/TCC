# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Determina se o colchao de dimensoes descritas na lista 'medidas' passa nas portas de
    dimensoes H(altura) e L(largura).
    list,int,int->bool"""
    porta_maior_dim = max(H,L)
    porta_menor_dim = min(H,L)
    passa = True
    if (porta_maior_dim < medidas[1] or porta_menor_dim < medidas[0]):
        passa = False
    return passa