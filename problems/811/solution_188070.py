def colchao(medidas, H, L):
    '''Funcao que dadas as medidas A,B e C (em ordem crescente)de um colchão, retornara True caso seja possivel passa-lo pela porta e False caso nao seja.'''
    if medidas[0]<L and medidas[1]<=H:
        return True 
    elif medidas[0]<L and medidas[1]>=H:
        return False 
    elif medidas[0]>L and medidas[1]<=H:
        return False 
    elif medidas[0]>L and medidas[1]>=H:
        return False
    elif medidas[1]>H:
        U=math.sqrt(H**2+L**2)
        t=(U/H)*medidas[0]
        L2=L-t
    if math.sqrt(L2**2+t**2)>B
        return True
    else:
        return False