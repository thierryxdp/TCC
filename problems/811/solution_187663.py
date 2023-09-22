def colchao(medidas,H,L):
    '''Os parametros de entrada sao uma lista com as dimensoes A, B e C do colch ̃ao em centımetros,
       ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a
       largura das portas em centımetros.
       A sua funcao deve retornar True se o colchao passa pelas portas e False em caso contrario.'''
        if medidas[1]<= H or medidas[1]<= L and medidas[0]<= L:
        return True
    else:
        return False