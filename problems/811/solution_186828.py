# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao (medidas,H,L):
    if (medidas[1] <= H <= medidas[2] or medidas[1] < L < medidas[2]):
        return True
    else:
        return False