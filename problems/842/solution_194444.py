def pontos_por_time(list1):
    '''[['Vasínthians', 'Fluminantos', [3,5]], ['Fluminantos', 'Varsínthians', [5,1]]]'''
    dic = {list1[0][0] : 0, list1[0][1]: 0}

	#primeiro jogo
    if(list1[0][2][0] > list1[0][2][1]):
        dic[list1[0][0]] = 3
        
    if(list1[0][2][0] < list1[0][2][1]):
        dic[list1[0][1]] = 3
        
    if(list1[0][2][0] == list1[0][2][1]):
        dic[list1[0][0]] = 1
        dic[list1[0][1]] = 1
        
    #segundo jogo
    if(list1[1][2][0] > list1[1][2][1]):
        dic[list1[1][0]] = 3
        
    
    if((list1[1][2][0] < list1[1][2][1])):
        dic[list1[1][1]] = 3
        
    if(list1[1][2][0] == list1[1][2][1]) :
        dic[list1[1][0]] = 1
        dic[list1[1][1]] = 1
        
    return dic