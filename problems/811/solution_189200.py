# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if H < L:
        if a < H:
            if b < L or c < L:
                return True
            else:
                return False
        elif b < H:
            if a < L or c < L:
                  return True
            else:
                return False
        elif c < H:
            if a < L or b < L:
                  return True
            else:
                return False
    elif L < H:
        if a < L:
            if b < H or c < H:
                return True
            else:
                return False
        elif b < L:
            if a < H or c < H:
                  return True
            else:
                return False
        elif c < L:
            if a < H or b < H:
                  return True
            else:
                return False