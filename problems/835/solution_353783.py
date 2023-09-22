def melhor_volta(m):
    '''
    '''
    linha=6
    coluna=10
    tempo=[]
    
    for i in range(linha):
        for j in range(coluna):
            if m[i][j]==m[i]:
                tempo.append(j)