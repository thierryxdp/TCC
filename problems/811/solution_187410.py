def colchao(medidas,H,L):
    '''
    função que calcula se o colchão tem medidas que o permitem passar pela portão;
    list,int,int  -> bool
    '''

    if max(medidas) < H and min(medidas) < L:
        return True
    
    else:
        return False