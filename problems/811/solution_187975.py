# Coloque um comentário dizendo o que a função faz
def colchao(medidas,H,L):
    m = medidas
    if (m[0] + m[1] + m[2]) / 3 < (H + L) / 2:
        return True