# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[1]<H or medidas[1]<L and medidas[0]<L:
        return True
    else:
        return False