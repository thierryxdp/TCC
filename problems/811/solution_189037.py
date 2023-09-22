# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    porta=[[medidas[0],medidas[1],medidas[2]],h,l]
    area1=medidas[0]*medidas[1]*medidas[2]
    area2=h*l
    if area1>area2:
        return True
    else:
        return False