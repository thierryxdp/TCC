def colchao(medidas, H, L):
    '''Função que informa se um colchao com uma determinada medida passa em um espaçp'''
    'list,int,int -> boll'
    medidas = medidas[0], medidas[1], medidas[2]
    
    A=int(medidas[0])
    B=int(medidas[1])
    C=int(medidas[2])
    D1 = (H * L)
    M = (A*B*C)
            
    if B  < H and C > H:
        
        return True