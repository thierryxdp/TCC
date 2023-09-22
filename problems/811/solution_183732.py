# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    list(medidas)
    a = medidas[0]
    b = medidas[1]
    if a<=H and b<=L or a<=L and b<=H:
        return True
    else:
        return False