#Start your python function here
def pontos_por_time(list1, list2)
	dic = {list1[0][0] : 0, list1[0][1]: 0}

	#primeiro jogo
    if(list1[0][2][0] > list1[0][2][1]):
        dic[list1[0][0]] = 3
    elif((list1[0][2][0] < list1[0][2][1])):
        dic[list1[0][1]] = 3
    else:
        dic[list1[0][0]] = 1
        dic[list1[0][1]] = 1
        
    #segundo jogo
        if(list2[0][2][0] > list2[0][2][1]):
        dic[list2[0][0]] = 3
    elif((list2[0][2][0] < list2[0][2][1])):
        dic[list2[0][1]] = 3
    else:
        dic[list2[0][0]] = 1
        dic[list2[0][1]] = 1
        
    return dic