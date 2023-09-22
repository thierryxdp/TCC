def colchao(medidas,H,L):
    '''Dados os parâmetros de entrada, uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros, retorna True se o colchão passa pelas portas e False caso contrário'''
    lc=medidas[0]
    ac=medidas[2]
    cc=medidas[1]
    if lc<=H and ac<=L and cc>=H or cc>=L:
        return True
    elif lc<=L and ac<=H and cc>=H or cc>=L:
        return True
    elif ac<=L and lc<=H and cc<=H or cc<=L:
        return True 
    elif ac<=H and lc<=L and cc<=H or cc<=L:
        return True
    elif cc<=L and ac<=L and lc>=H or lc>=L:
        return True
    elif cc<=L and ac<=H cc<=H or cc<=L:
        return True
    elif ac>H and lc<H or ac>L and lc<H or ac>H and cc<L or ac>L and cc<H or bc>H and cc<L or bc<L and cc>H :
        return False