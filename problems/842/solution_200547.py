#Start your python function here
def pontos_por_time(resultados):

    ''' '''

    #

    pts1 = 0

    pts2 = 0

    if resultados[0][0][2][0] > resultados[0][0][2][1]:

        

        pts1 = pts1 + 3

    elif resultados[0][0][2][0] < resultados[0][0][2][1]:

        pts2 = pts2 + 3
    
    elif resultados[0][0][2][0] == resultados[0][0][2][1]:

        pts1 = pts1 + 1, pts2 = pts2 + 1