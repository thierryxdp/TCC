def colchao(medidas,H,L):
    '''
    função que calcula se o colchão tem medidas que o permitem passar pela portão;
    list,int,int  -> bool
    '''

    if (medidas)[0] < H and (medidas)[0] < L and (medidas)[1] < H or (medidas)[1] < L:
        return True
    if (medidas)[1] < H and (medidas)[1] < L and (medidas)[2] < H or (medidas)[2] < L:
        return True
    if (medidas)[0] < H and (medidas)[0] < L and (medidas)[2] < H or (medidas)[2] < L:
        return True
          
    else:
        return False