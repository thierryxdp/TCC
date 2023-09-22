# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[1]==L or medidas[1]<L:
        return True
    elif medidas[1]==H or medidas[1]<H:
        return True
    elif medidas[2]==L or medidas[2]<L:
        return True
    elif medidas[2]==H or medidas[2]<H:
        return True
    else:
        return False