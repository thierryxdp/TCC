# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    c1 = medidas[1] < H
    c2 = medidas[1] < L
    c3 = medidas[2] < H
    c4 = medidas[2] < L
    return c1 and c3 or c2 and c4