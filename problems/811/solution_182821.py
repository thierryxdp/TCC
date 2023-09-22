# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=H and B<=L:
        return True
    if A<=L and B<=H:
        return True
    if A<=H and C<=L:
        return True
    if A<=L and C<=H:
        return True
    if B<=L and C<=H:
        return True
    if B<=H and C<=L:
        return True
    else:
        return False