def conta_numero(num,m):
    '''dado um num int, conta e retorna quantas vezes o num aparece
    na matriz
    int, list -> int'''
    
    cont = 0
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==num:
                cont+=1
                
    return cont