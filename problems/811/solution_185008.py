def colchao(medidas,H,L):
    """Função que dado uma lista com as dimensões A, B, C do colchão em centímetros, e dois
    inteiros H (altura) e L (largura) das portas em centímetros, retorna o booleano 'True' se o
    colchão passa pelas portas e 'False' em caso contrário; list, int, int -> bool  """

    A,B = medidas[0],medidas[1]
       
    if (B<=H and A<=L) or (B<=L and A<=H):
        return True
    else:
        return False