def media_matriz(m):
    '''dada uma matriz de int nao vazia, retorna a media
    de todos os num da matriz
    lis -> float'''
    
    num=0
    n=0
    
    for i in m:
        num = num + sum(i)
        n = n + len(i)
        
    return round(num/n,2)