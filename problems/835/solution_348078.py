def melhor_volta(mat):
    '''Função que recebe uma matriz 6x10 com os tempos dos corredores em cada volta;
retorna uma tupla dizendo de quem foi a melhor volta, com qual tempo e em que volta.
list(list)->tupla'''
    l= [0,0,0]
    t=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            t.append(mat[i][j])
        m = min(t)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==m:
                    l[0]=i+1
                    l[1]=mat[i][j]
                    l[2]=j+1
    return tuple(l)