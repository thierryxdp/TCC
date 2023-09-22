# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if (H<medidas[0] or L<medidas[0]):
        return False
    elif (medidas[0]<H and L<medidas[1]):
        return False