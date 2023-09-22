def colchao(medidas,H,L):
    ''' a função calcula se um colchão dadas as entradas passa
    em uma porta ou não
    list,int,int->bool
    '''
    if medidas[2]<=H:
        return True
    elif medidas[1]<=H:
        return True
    elif medidas[1]>H and (medidas[1]*medidas[2])<H*L:
        return True
    else:
        return False

# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis