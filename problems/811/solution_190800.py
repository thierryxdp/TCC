# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,h,l):
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    if ((a<h) and (c<l)) or ((a<l) and (c<h)):
        return True
    else:
        return False
    if ((a<h) and (b<l)) or ((a<l) and (b<h)):
        return True
    else:
        return False
    if ((b<h) and (c<l)) or ((b<l) and (c<h)):
        return True
    else:
        return False