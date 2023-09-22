def colchao(medidas,H,L):
    '''Dados os parâmetros de entrada, uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros, retorna True se o colchão passa pelas portas e False caso contrário'''
    a=medidas[1]
    b=medidas[2]
    c=medidas[0]
    if (a*b)>(H*L) or (c*b)>(H*L):
        return False
    if (c*b)<(H*L):
        return True
    elif (c*b)==(H*L):
        return True
    elif (a*b)<(H*L):
        return True 
    elif (a*b)==(H*L):
        return True 
    if (a*b)>(H*L) or (c*b)>(H*L):
        return False