def colchao((A,B,C),H,L):
    '''Esta função define se o colchão passa, dado:
    dict(str, list), str, str -->
    '''
    medidas = [A,B,C]
    
    if medidas[1] <= H or medidas[2] <= L:
        return 'True' 
    else:
        return 'False'