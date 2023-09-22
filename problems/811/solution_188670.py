# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    medidas = []
    H = []
    L = []
    if (medidas[0] <= H[0]) and (medidas[1] <= L[0]):
        return True
    else:
        return False