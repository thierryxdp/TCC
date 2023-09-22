# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,h,l):
    if medidas[0]*medidas[1]<=h*l:
        return True
    else:
        return False
    if medidas[0]*medidas[2]<=h*l:
        return True
    else:
        return False
    if medidas[1]*medidas[2]<=h*l:
        return True
    else:
        return False