def colchao(medidas, H, l):
    '''
    '''
    if medidas[1]<H and medidas[2]>l:
        return 'True'
    
    elif medidas[1]>H and medidas[2]>l:
        return 'False'
    
    elif medidas[1]<=H and medidas[2]>l:
        return 'True'
    
    elif medidas[1]>H and medidas[2]<=l:
        return 'True'