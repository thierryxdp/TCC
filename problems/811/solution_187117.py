# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[0]>=L or medidas[1]<=H or medidas[2]<=H:
        return True
    elif medidas[0]>=L or (medidas[1]>H and medidas[2]<=H):
        return True
    else:
        return False