def colchao(medidas,H,L):
    '''Função que calcula as dimensões de uma porta e de um colchão e retorna se é possivel esse
    colchao passar pela porta ou não
    list,int,int -> bool'''
    medidas = [a,b,c]
    if a>H or a>L and b>H or b<=H and b>L or b<=L and c>H or c<=H and c>L or c<=L:
        return False
    if a<=H or a<=L and b<=H or b<=L and c<=H or c<=L:
        return True