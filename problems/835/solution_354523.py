def melhor_volta(m):
    '''retorna de quem foi a melhor volta, com qual tempo e em que volta;
    mat->tuple'''
    tempo=()
    volta=0
    corredor=0
    
    for i in range(7):
        for j in range(11):
            tempo+=(j,)

    for i in range(7):
        for j in range(11):
            if m[i][j]==min(tempo):
                volta=i
                corredor=j

    return (corredor,min(tempo),i)