# Coloque um comentário dizendo o que a função faz
def colchao(medidas,H,L):
    m = medidas
    if (m[1]+m[2])/2 <= (H+L)/2:
        return True
    if (m[1]+m[2])/2 > (H+L)/2:
        return False