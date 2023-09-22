def colchao(medidas,H,L):
    '''Esta função define se o colchão passa, dado:
    dict(str, list), str, str -->
    '''
    medidas = [A,B,C]
    
    if medidas[0] <= H or medidas[1]:
        return 'True' 
    else:
        return 'False'