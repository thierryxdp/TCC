#Start your python function here
def pontos_por_time(list1): 
    """Função que dá os pontos por cada time"""

    dicio = {list1[0][0] : 0, list1[0][1]: 0}

	#primeiro jogo
    if(list1[0][2][0] > list1[0][2][1]):
        dicio[list1[0][0]] = 3
        
    if(list1[0][2][0] < list1[0][2][1]):
        dicio[list1[0][1]] = 3
        
    if(list1[0][2][0] == list1[0][2][1]):
        dicio[list1[0][0]] = 1 
        dicio[list1[0][1]] = 1
        
    #segundo jogo
    if(list1[1][2][0] > list1[1][2][1]):
        dicio[list1[1][0]] = dicio[list1[1][0]] + 3
        
    
    if((list1[1][2][0] < list1[1][2][1])):
        dicio[list1[1][1]] = dicio[list1[1][1]] + 3
        
    if(list1[1][2][0] == list1[1][2][1]) :
        dicio[list1[1][0]] = dicio[list1[1][0]] + 1
        dicio[list1[1][1]] = dicio[list1[1][1]] + 1
        
    return dicio