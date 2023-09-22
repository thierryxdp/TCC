def colchao(medidas, H, l):
    '''
    '''
    if medidas[1]>H:
        return 'False'
    
    elif H>medidas[1] and medidas[2]<l:
        return 'True'
    
    else:
        return 'True'