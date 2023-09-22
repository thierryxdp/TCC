def colchao(medidas,H,L):
    """funcao que, dada uma list chamada medidas, com as dimensoes do colchai
    A, B e C, ordenadas da menor para a maior, e dois inteiros H(altura) e L(largura)
    da porta, retorna True se o colchao passa pela porta, e retorna
    False se o colchao nao passa pela porta
    list,int,int -> bool"""
    if (medidas[0] <= L and medidas[1] <= H) or (medidas[0] <= H and medidas[1] <= L):
        return True
    else:
        return False