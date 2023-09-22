def colchao(dimensoes,H,L):
    '''função que dada uma lista com as dimensões A, B e C do colchão em
    centímetros, ordenadas da menor pra maior, e dois inteiros H e L, cor-
    respondentes respectivamente à altura e à largura da porta em centímetros;
    list, int, int -> bool'''
    if dimensoes[1] <= H:
        return True
    else:
        return False