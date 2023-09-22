def melhor_volta(matrix):
    '''função que recebe os tempos dos corredores em cada volta e retorna a melhor volta,o tempo e em qual volta
    list->tuple'''
    corredores=[matrix[0],matrix[1],matrix[2],matrix[3],matrix[4],matrix[5]]
    i=0
    voltas=[]
    while i<10:
        j=0
        while j<6:
            if corredores[j][i] == min([matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i],matrix[4][i],matrix[5][i]]):
                list.append(voltas,[j+1,corredores[j][i],i+1)
            j+1                        
    return voltas