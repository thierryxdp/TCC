def colchao(medidas,H,L):

    """ Dados as medidas(A,B,C) de um colchao e as medidas(H,L) de uma porta, retorna se o colchao passaria ou não pela porta com uma de suas faces obrigatoriamente paralelas ao chao;

    lista,int,int->bool """

    if medidas[1]<=L and medidas[2]<=H:

        return True

    if medidas[2]>H and medidas[1]<=L:

        return True

    if medidas[1]<=H:

        return True

    else:

        return False