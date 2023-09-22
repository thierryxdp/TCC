# Coloque um comentário dizendo o que a função faz
def colchao(medidas,H,L):
    m = medidas
    if (m[1]*m[2]) <= (H*L) or m[1] <= H :
        return True
    if (m[1]*m[2]) > (H*L):
        return False