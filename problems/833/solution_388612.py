def conta_numero(n,m):
    '''retorna quantas vezes um número aparece na matriz;
    int,mat->int'''
    
    lista=[]
    
    for i in m:
        if i == n:
            lista+=i
            
    return len(lista)