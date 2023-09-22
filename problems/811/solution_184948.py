# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,altura_porta,L):
    if medidas[0]>H and medidas[1]>L or medidas[2]>L:
        return True
    elif medidas[0]>L and medidas[1]>H or medidas[2]>H:
        return True
    elif medidas[1]>H and medidas[0]>L or medidas[2]>L:
        return True
    elif medidas[1]>L and medidas[0]>H or medidas[2]>H:
        return True
    elif medidas[2]>H and medidas[0]>L or medidas[1]>L:
        return True
    elif medidas[2]>L and medidas[0]>H or medidas[1]>H:
        return True
    else:
        return False