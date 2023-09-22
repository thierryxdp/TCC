def colchao(medidas, H, L):
    '''Função que informa se um colchao com uma determinada medida passa em um espaçp'''
    'list,int,int -> boll'
    medidas = list(medidas)
    medidas = medidas[0], medidas[1], medidas[2]
    
    A=int(medidas[0])
    B=int(medidas[1])
    C=int(medidas[2])
    H=int()
    L=int()
    D1 = (H * L)%2
    
    M = (A*B*C)%3  
        
    if D1 < M:
        return  True