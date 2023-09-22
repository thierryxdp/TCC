# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,h,l):
    porta=h*l
    if medidas[0]*medidas[1]<=porta:
        return True
    elif medidas[0]*medidas[2]<=porta:
        return True
    elif medidas[1]*medidas[2]<=porta:
        return True
    else:
        return False