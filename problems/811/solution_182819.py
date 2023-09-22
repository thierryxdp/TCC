# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    A=medidas[0]
    B=medidadas[1]
    C=medidas[2]
    if A<=H and B<=L:
        return true
    if A<=L and B<=H:
        return true
    if A<=H and C<=L:
        return true
    if A<=L and C<=H:
        return true
    if B<=L and C<=H:
        return true
    if B<=H and C<=L:
        return true
    else:
        return false