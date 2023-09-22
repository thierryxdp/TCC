def colchao(medidas,H,L):
    '''Função que retorna True se o colchão passa pelas portas e False em caso contrário, dado as medidas do colchão, a altura H das portas e a largura L das portas; list[int,int,int],int,int'''
    if (medidas[0]*medidas[1])<=(H*L) and (medidas[1]<=H or medidas[1]<=L):
        return True
    elif (medidas[0]*medidas[1])>(H*L) or medidas[1]>H or medidas[1]>L:
        return False