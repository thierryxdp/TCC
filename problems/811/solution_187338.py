# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''Coloque as medidas do seu colchão(medidas) e as medidas da sua porta(H e L) e saiba se o colchão passará ou não pela porta'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if H>=medidas[0] and L>=medidas[1]:
        return True
    if H>=medidas[1] and L>=medidas[0]:
        return True
    else:
        return False