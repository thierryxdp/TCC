def colchao(medidas, H, l):
    '''
    '''
    if medidas[1]>H:
        return 'False'
    
    elif medidas[1]>H and medidas[2]<l:
        return 'True'
    
    else:
        return 'True'