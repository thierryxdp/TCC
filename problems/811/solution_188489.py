# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[1] <= H:
        return True
    elif medidas[2] < L:
        return True
    elif medidas[1] > H:
        return False