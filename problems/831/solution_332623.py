def lingua_p(x):
    ''' Função que dado uma palavra, retorna uma palavra na lingua do p
    ass: str-->str'''
    i=0
    while i < len(x):
        if x[i] in 'aeiouAEIOU':            
            b=str.partition(x,x[i])
            c=b[0]+'p'+b[1]+b[2]
        i=i+1    
    return c