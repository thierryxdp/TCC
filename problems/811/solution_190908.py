def colchao(medidas,H,L):
    '''Dados os parâmetros de entrada, uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros, retorna True se o colchão passa pelas portas e False caso contrário'''
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    if (c*b)<(H*L):
        return True
    elif (c*b)==(H*L):
        return True
    elif (a*b)<(H*L):
        return True 
    elif (a*b)==(H*L):
        return True 
    else:
        return False