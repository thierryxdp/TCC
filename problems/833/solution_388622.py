def conta_numero(n,m):
    '''retorna quantas vezes um número aparece na matriz;
    int,mat->int'''
    
    qntd=0
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == n:
                qntd=qntd+m[i][j]
            
    return qntd/n