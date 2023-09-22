def posLetra(x,l,n):
    ''' função que dada uma str, uma substr e sua ocorrência
    retorna seu índice se possivel e se não retorna -1
    str,str,int>int'''
    if str.count(x,l)<n:
        return -1
    
    indices=()
    proximo=0
    
    while proximo<len(x):
        if x[proximo]==l:
            indices=indices+(proximo,)
        proximo=proximo+1
        
    return indices[n-1]