def colchao(medidas,H,L):
    '''Esta função define se o colchão passa, dado:
    dict(str, list), str, str -->
    '''
    
    if medidas[1] <= H or medidas[2] <= L:
        return 'True' 
    else:
        return 'False'