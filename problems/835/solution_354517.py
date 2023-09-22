def melhor_volta(m):
    '''retorna de quem foi a melhor volta, com qual tempo e em que volta;
    mat->tuple'''
    tempo=[]
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            tempo+=[m[i][j],]

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==min[tempo]:
                volta=i
                corredor=j

    return (corredor,min[tempo],i)