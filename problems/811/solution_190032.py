def colchao(medidas,H,L):
    '''Esta função define se o colchão passa, dado:
    - A = altura
    - B = largura
    - C = comprimento 
    - H = altura
    - L = largura
    int,int,int,int,int-->str'''
    
    medidas == [A,B,C]
    #[A,B,C],H,L
    
    if B <= H:
        return 'True' 
    else:
        return 'False'