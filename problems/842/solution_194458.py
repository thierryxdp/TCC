def pontos_por_time(list1):
    '''função que faz a contabilidade de pontos de cada time informado, dados os times e os gols em cada partida
    	Lista[] -> Dicionario{}''' 

    dic = {list1[0][0] : 0, list1[0][1]: 0}

	#primeiro jogo
    if(list1[0][2][0] > list1[0][2][1]):
        dic[list1[0][0]] = dic[list1[0][0]] + 3
        
    if(list1[0][2][0] < list1[0][2][1]):
        dic[list1[0][1]] = dic[list1[0][1]] + 3
        
    if(list1[0][2][0] == list1[0][2][1]):
        dic[list1[0][0]] =dic[list1[0][0]] + 1 
        dic[list1[0][1]] =dic[list1[0][1]] + 1
        
    #segundo jogo
    if(list1[1][2][0] > list1[1][2][1]):
        dic[list1[1][0]] = dic[list1[1][0]] + 3
        
    
    if((list1[1][2][0] < list1[1][2][1])):
        dic[list1[1][1]] = dic[list1[1][1]] + 3
        
    if(list1[1][2][0] == list1[1][2][1]) :
        dic[list1[1][0]] = dic[list1[1][0]] + 1
        dic[list1[1][1]] = dic[list1[1][1]] + 1
        
    return dic