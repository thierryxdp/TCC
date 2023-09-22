def colchao(A,B,C,H,L):
    '''Função que retorna true quando o colchão da promoção passa pela porta de João
	e retorna False quando o colchão não passa pela porta de João.
    int,int,int,int,int-->bool'''
    medidas = [A,B,C]
    if medidas[0] <= L and medidas[1] <= H:
        return True
    else:
        return False