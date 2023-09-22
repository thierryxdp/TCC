# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''colchao recebe as medidas(dimensões do colchão axbxc) a altura H e largura L da porta da sua casa, e devolve se o colchão com as determinadas medidas passa ou não pela porta de sua casa.
    list,float,float-->bool'''
    [a,b,c]=medidas
    if a<=L and (b<=H or c<=H):
        return True
    else:
        return False