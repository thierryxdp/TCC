def conta_numero(n, m):
    ''' Função verifica se o numero inteiro n está na matriz m e quantas vezes ele aparece.
    int, list -> int'''
    c=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            b=m[i][j]
            if(b==n):
                c=c+1
    return c