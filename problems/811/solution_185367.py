def colchao(medidas,H,L):
    '''Funcao que retorna se é possível um colchão com medidas AxBxC passar por 
uma porta com dimensões H e L, em centímetros.
list,int,int->bool'''
    x=medidas
    if x[1]<=H or x[1]<=L:
        return True
    if x[2]<=H or x[2]<=L:
        return True
    else:
        return False