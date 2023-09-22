# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[0]*medidas[1]<(medidas[0]*medidas[2] and
    medidas[1]*medidas[2]):
        ladoinf=medidas[0]*medidas[1]
    if medidas[0]*medidas[2]<(medidas[0]*medidas[1] and
    medidas[1]*medidas[2]):
        ladoinf=medidas[0]*medidas[2]
    if medidas[1]*medidas[2]<(medidas[0]*medidas[1] and
    medidas[0]*medidas[2]):
        ladoinf=medidas[1]*medidas[2]
    if ladoinf<= H*L:
        return True
    if ladoinf>H*L:
        return False