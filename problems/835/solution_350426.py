def melhor_volta(tempo):
    '''função que dada, uma matriz com os tempos de cada 
    corredor de uma corrida, retorna uma tupla informando
    de quem foi a melhor volta e com qual tempo. list-> tuple'''
    listagem=[0,float('inf'),0]
    for i in range(6):
        for j in range(10):
            if tempo[i][j]<listagem[1]:
                listagem=i+1,tempo[i][j],j+1
    return listagem