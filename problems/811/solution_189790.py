def colchao(medidas,H,L):
    '''Esta função preve se um colchão de medidas AxBxC em ordem crescente passa pela porta de João.
    list,int,int-->bool'''
    if (medidas[1]<=L and medidas[2]<=H)or medidas[1]<=L or medidas[2]<=H or (medidas[0]<L and medidas[1]<=H):
        return True
    else:
        return False