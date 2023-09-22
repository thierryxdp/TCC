def colchao(medidas,H,L):
    '''Função que calcula as dimensões de uma porta e de um colchão e retorna se é possivel esse
    colchao passar pela porta ou não
    list,int,int -> bool'''
    medidas == [a,b,c]
    if medidas[0]>H or medidas[0]>L and medidas[1]>H or medidas[1]<=H and medidas[1]>L or medidas[1]<=L and medidas[2]>H or medidas[2]<=H and medidas[2]>L or medidas[2]<=L:
        return False
    if medidas[0]<=H or medidas[0]<=L and medidas[1]<=H or medidas[1]<=L and medidas[2]<=H or medidas[2]<=L:
        return True