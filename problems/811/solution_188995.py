# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[0] < H:
        if medidas[1] < L or medidas[2] < L:
            return True
    if medidas[1] < H:
        if medidas[0] < L or medidas[2] < L:
            return True
    if medidas[2] < H:
        if medidas[0] < L or medidas[1] < L:
            return True
        else:
            return False
    else:
        return False