# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[1] > L:
        return False
    if medidas[2] > H:
        return False
    else:
        return True