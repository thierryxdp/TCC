# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=H and B<=H or A<=L and B<=L:
        return True
    else:
        return False