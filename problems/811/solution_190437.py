def colchao(dimensoes,H,L):
    '''Função que retorna  se o colchão passa pela porta de dimensões H(altura) e L(largura), o valor de entrada dimensões uma lista contendo as  dimensões do colchão que são A,B e C(H e L são números inteiros)( A,B e C do colchão  em centímetros, ordenadas do menor para o maior)'''
        if dimensoes[1]<=L and dimensoes[0]<=H:
            return True
        elif dimensoes[0]<=L and dimensoes[2]<=H:
            return True
        elif dimensoes[2]<=L and dimensoes[1]<=H:
            return True
        elif dimensoes[0]<=L and dimensoes[1]<=H:
            return True
        else:
            return False