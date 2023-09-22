# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    caso1 = medidas[0] < H and medidas[1] < L
    caso2 = medidas[1] < H and medidas[2] < L
    caso3 = medidas[0] < H and medidas[2] < L
    return caso1 or caso2 or caso3