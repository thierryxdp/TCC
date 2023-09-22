def colchao(medidas, H, l):
    '''
    Funcao que recebe as medidas de um colchao e de uma 
    porta e define se as medidas do colchao deixam o mesmo
    passar pela porta 
    list, int, int -> bool
    '''
    if medidas[1]<H and medidas[2]<l:
        return 'True'
    
    elif medidas[1]>H and medidas[2]>l:
        return 'False'
    
    elif medidas[1]<=H and medidas[2]>l:
        return 'True'
    
    elif medidas[1]>H and medidas[2]<=l:
        return 'True'