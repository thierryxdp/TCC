def media_matriz(x):
    '''
    dada uma matriz de int não vazia, retorna a media de todos os numeros da matriz (2 casas de precisão)
    list->float 
    '''
    s=0
    for n in range(len(x)):
        m=x[n]
        for k in range(len(m)):
            s=s+m[k]
    med=(s/(len(x)*len(x[0])))        
    return round(med,2)