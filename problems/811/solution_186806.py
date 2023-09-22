def colchao(medidas,H,L):
    ''' retorna se o colchao com medidas med, que deverao estar ordenada em forma crescente, consegue passar pela porta de altura H e largura L'''
    '''int,int,int,int,int -> str'''
    
    if medidas[0] <= L and medidas[1] <= H :
        return True
    
    else:
        return False