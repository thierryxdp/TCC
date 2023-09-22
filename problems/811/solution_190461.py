# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,h,l):
    #porta=h*l
    #if medidas[0]*medidas[1]<=porta:
    #    return True
    #elif medidas[0]*medidas[2]<=porta:
    #    return True
    #elif medidas[2]*medidas[1]<=porta:
    #    return True
    if medidas[0]>h or medidas[0]>l:
        return False
    elif medidas[1]>h or medidas[1]>l:
        return False
    elif medidas[2]>h or medidas[2]>l:
        return False
    else:
        return True