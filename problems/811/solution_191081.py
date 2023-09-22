def colchao(medidas,H,L):
    '''Dados os parâmetros de entrada, uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros, retorna True se o colchão passa pelas portas e False caso contrário'''
    lc=medidas[0]
    ac=medidas[2]
    cc=medidas[1]
    if cc <= H or cc <=L:
        return True
    elif ac <= H or ac<=L:
        return True
    elif lc<=L and lc<=H:
        return False