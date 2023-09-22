# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """list, int, int -> bool"""
    if medidas[2] > H or medidas[1] > L:
        teste = True
    elif medidas[2] > L or medidas[1] > H:
        teste = True
    else:
        teste = False
    return teste