def colchao(medidas,H,L):
    '''Dados os parâmetros de entrada, uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros, retorna True se o colchão passa pelas portas e False caso contrário'''
    lc=medidas[1]
    ac=medidas[2]
    cc=medidas[0]
    if lc<=H and ac<=L:
        return True
    elif ac<=H and lc<=L:
        return True
    elif ac<=L and lc<=H:
        return True 
    elif ac<=H and lc>=L:
        return False
    elif ac<=L or lc<=L:
        return True