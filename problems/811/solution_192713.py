# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    A, B, C = medidas
    if A < H or B < H or C < H and A < L or B < L or C < L:
        return True
    else:
        return False