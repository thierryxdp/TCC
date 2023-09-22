# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if (H<medidas[0] or L<medidas[0]):
        return False
    elif ((medidas[0]<H<medidas[1] and L<medidas[2]) or (medidas[0]<L<medidas[1] and H<medidas[2])):
        return False
    elif ((medidas[1]<H and L<medidas[2]) or (medidas[1]<L and H<medidas[2])):
        return False
    else:
        return True