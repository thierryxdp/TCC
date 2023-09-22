def colchao(x,H,L):
    '''
        onde x[A, B, C]
    '''
    if x[1]<= H and x[0]<= L:
        return True
    elif x[2]<= H and x[0]<= L:
        return True
    else:
        return False# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis