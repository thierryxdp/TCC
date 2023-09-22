# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    x=medidas[0]
    y=medidas[1]
    z=medidas[2]
    if x <= H:
        if y < L:
            return True
        else:
            continue
    elif x < L:
        if y < H:
            return True
    else:
        return False