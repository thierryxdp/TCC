# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef colchao(col, h, l):
def colchao(medidas,H,L):
    '''Dada um lista com as dimensões do colcão, e
    list,float,float -> bool'''
    if medidas[1] <= H:
     	return True
    elif medidas[2] <= H:
        return True
    else:
        return False