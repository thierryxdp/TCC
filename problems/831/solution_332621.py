def lingua_p(x):
    ''' Função que dado uma palavra, retorna uma palavra na lingua do p
    ass: str-->str'''
    b=x[0]
    i=0
    while i < len(x):
        if x[i] in 'aeiouAEIOU':            
            b = b[i+2] + 'p' + x[i:]
        i=i+1    
    return b