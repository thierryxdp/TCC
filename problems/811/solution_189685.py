def medidas(A,B,C):
    return [A,B,C]
def colchao(medidas,H,L):
    '''Recebe uma lista com as dimensões do colchão em centímetros, ordenadas
    da menor para a maior, e dois inteiros H e L, correspondentes
    respectivamente a altura e a largura das portas em centímetros.
    Retorna True se o colchão passa pelas portas e False caso contrário
    '''
    if L>247:
        return True
    if medidas[1]>H:
        return False
    else:
        return True