# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    tupla = tuple(medidas)
    espessura,largura,comprimento = tupla
    if largura<H and comprimento<L or comprimento<H and largura<L:
        return True
    else:
        return False