# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    medidas = []
    if medidas[1] <= H:
        return True
    elif medidas[2] <= L:
        return True
    else:
        return False