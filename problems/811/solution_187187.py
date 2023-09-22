def colchao(medidas,H,L):
    '''verifica se o colchao de medidas [a,b,c] passa pela porta de medidas H e L
    a<b<c
    H = altura
    L = largura
    list, int, int -> bool'''
    [a,b,c]=medidas
    if c>H and b>L or c>H and a>L or c>L and b>H or c>L and a>H :
        return False
    else:
        return True