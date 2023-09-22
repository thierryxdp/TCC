def colchao(medidas,H,L):
    '''Funcao que retorna se e possivel um colchao de dimensao AxBxC
    passar por uma porta de altura H e largura L.
    list,int,int->bool'''
    x=medidas
    if x[1]<=H or x[1]<=L:
        return True
    if x[2]<=H or x[2]<=L:
        return True
    else:
        return False