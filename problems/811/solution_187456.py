def colchao(medidas,H,L):
    """ Dadas as medidas AxBxC do colchao ,e a altura H e a Largura L das portas,
    retorna True, se ela passa pela porta e False, se ela não passar.
    list,int,int->bool"""
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    if a<=L and b<=H or a<=H and b<=L:
        return True
    else:
        return False