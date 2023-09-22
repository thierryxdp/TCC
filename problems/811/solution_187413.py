def colchao(medidas,H,L):
    '''
    função que calcula se o colchão tem medidas que o permitem passar pela portão;
    list,int,int  -> bool
    '''

    if (medidas)[0:2] < H and (medidas)[0:2] < L:
        return True
    
    else:
        return False