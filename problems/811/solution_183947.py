# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    tupla = tuple(medidas)
    espessura,largura,comprimento = tupla
    if largura<H:
        return True
    else:
        return False