def colchao(medidas,H,L):
    '''Função que rece uma lista com as dimensões A x B x C de um colchão e dois inteiros
    que são a altura (H) e a largura(L) da porta e retorna True se o colchão passa pela
    porta e False caso contrário; list, int, int -> bool'''
    
    if medidas[1] > L and medidas[2] > H and medidas[1] > H:
        return False
    else:
        return True