def colchao(medidas,H,L):
    '''Função que recebe uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior,
    e dois inteiros H e L, correspondentes respectivamente a altura e largura das portas em centímetros.
    Retorna True se o colchão passa pelas portas e False caso contrário;
    list, int, int -> bool'''
    if medidas[1] <= H or medidas[1] <= L:
        return True
    else:
        return False