def colchao(medidas,H,L):
    '''Função que dados como parâmetros de entrada uma lista com as dimensões A, B e C do colchão em centímetros,
ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a
largura das portas em centímetros, retorna True se o colchão passa na porta ou False se não passa;
    list, int, int --> boolean'''
    if medidas[1]>H:
        return False
    else:
        return True