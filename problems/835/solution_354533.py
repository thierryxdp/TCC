def melhor_volta(m):
    '''retorna de quem foi a melhor volta, com qual tempo e em que volta;
    mat->tuple'''
    tempo=[]
    corredor=0
    volta=0
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            tempo+=[m[i][j],]
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==min(tempo):
                volta+=j
                corredor+=i

    return (volta,min(tempo),corredor)