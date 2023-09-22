# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if (medidas[0]<=H or medidas[0]<=L) and (medidas[1]<=L or medidas[1]<=H):
        return True
    else:
        return False