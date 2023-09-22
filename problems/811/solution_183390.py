# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[2]>H or medidas[1]>L:
        return False
    elif medidas[0]<L and medidas[1]<H: 
        return True