def melhor_volta(matriz):
    '''função  que dada uma matriz 6x10 retorna o menor tempo 
    junto com de quem foi a melhor volta e em que volta
    list->list'''
    tempo1=matriz[0,0]
    for i in range(1,7):
        for j in range(1,11):
            tempo2=matriz[i][j]
            if tempo1>tempo2:
                tempo1=tempo2
    for i in range(1,7):
        for j in range(1,11):
            if tempo1==matriz[i][j]:
                corredor=i+1
                volta=j+1
                return (tempo1,corredor,volta)