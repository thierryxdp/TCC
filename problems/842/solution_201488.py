def pontos_por_time(list1):
    if (type(list1) != list or len(list1) != 2 or type(list1[0]) != list or len(list1[0]) != 3 or type(list1[1]) != list or len(list1[1]) != 3):
        return false
    else:
        if(type(list1[0][0]) == str and type(list1[0][1]) == str and type(list1[0][2]) == list and len(list1[0][2]) == 2 and type(list1[0][2][0]) == int and type(list1[0][2][1]) == int and type(list1[1][0]) == str and type(list1[1][1]) == str and type(list1[1][2]) == list and len(list1[1][2]) == 2 and type(list1[1][2][0]) == int and type(list1[1][2][1]) == int ):
            teamA = 0
            teamB = 0
        
            if( list1[0][2][0] > list1[0][2][1] ):
                teamA = teamA + 3
            elif( list1[0][2][0] == list1[0][2][1] ):
                teamA = teamA + 1
                teamB = teamB + 1
            else:
                teamB = teamB + 3
         
            if( list1[1][2][0] > list1[1][2][1] ):
                teamB = teamB + 3
            elif( list1[1][2][0] == list1[1][2][1] ):
                teamB = teamB + 1
                teamA = teamA + 1
            else:
                teamA = teamA + 3
                
            return {list1[0][0]: teamA, list1[0][1]: teamB}
            
            
        else:
            return False