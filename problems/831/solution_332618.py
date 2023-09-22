def lingua_p(x):
    ''' Função que dado uma palavra, retorna uma palavra na lingua do p
    ass: str-->str'''
    b=x
    for i in x:
        if x[i] in 'aeiouAEIOU':            
            b=b[:x[i]]+x[i]+'p'+b[x[i]:]
            
    return b