def colchao(medidas,H,L):
    '''verifica se o colchao de medidas [a,b,c] passa pela porta de medidas H e L
    a<b<c
    H = altura
    L = largura
    list, int, int -> bool'''
    [a,b,c]=medidas
    if a>H or a>L or b>H:
        return False
    else:
        return True