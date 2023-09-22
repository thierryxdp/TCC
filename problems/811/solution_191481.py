# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    medidas.sort()
    if medidas[1]<H and medidas[2]<L:
        return True