def colchao(medidas,H,L):
    '''verifica se o colchao de medidas [a,b,c] passa pela porta de medidas H e L
    a<b<c
    H = altura
    L = largura
    list, int, int -> bool'''
    [a,b,c]=medidas
    if b>H and a>L or b>L and a>H or c>H and a>L or c>L and a>H or b>H and c>L or b>L and c>H:
        return False
    else:
        return True