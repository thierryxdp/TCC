def colchao(Dc,Dp):
    ''' dado as dimensões do colchão e da porta retorna se é possivel que este passe pela porta
    Dc: dimensões do colchão
    Dp: dimensões do colchão'''
    if Dc[1]>Dp[0] and Dc[2]>Dp[0]:
        return False
    else:
        return True