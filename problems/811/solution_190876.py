def colchao(medidas,H,L):
    '''Dados os parâmetros de entrada, uma lista com as dimensões do colchão em centimetros,ordene'''
    a= medidas[1]
    b= medidas[2]
    c= medidas[0]
    if (2*(a*b)+(b*c))<(H*L):
        return True
    elif (2*(a*b)+(b*c))==(H*L):
        return True
    else:
        return True