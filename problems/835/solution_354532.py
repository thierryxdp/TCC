def melhor_volta(m):
    '''retorna de quem foi a melhor volta, com qual tempo e em que volta;
    mat->tuple'''
    tempo=[]
    corredor=0
    volta=0
    
    for i in range(1,7):
        for j in range(1,11):
            tempo+=[m[i][j],]
    
    for i in range(1,7):
        for j in range(1,11):
            if m[i][j]==min(tempo):
                volta+=j
                corredor+=i

    return (volta,min(tempo),corredor)