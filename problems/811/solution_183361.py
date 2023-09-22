# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[0]<H and medidas[1]<L:
        return True
    elif medidas[1]<H and medidas[0]<L:
        return True
    else:
        return False