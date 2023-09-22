def pontos_por_time(resultados):
    
    confronto1=resultados[0]
    confronto2=resultados[1]
    jogo1=confronto1[2]
    jogo2=confronto2[2]
    placares=jogo1+jogo2
    

    def pontos_time1(placares):
        if placares[0]>placares[1]and placares[3]>placares[2]:
            return 6
        elif:
            placares[0]==placares[1]and placares[3]==placares[2]:
                return 2
            else:
                if placares[0]<placares[1]and placares[3]<placares[2]:
                    return 0
                elif(placares[0]>placares[1]or placares[3]>placares[2])and (placares[0]<placares[1]or placares[3]<placares[2]):
                    return 3
                else:
                    if(placares[0]>placares[1]or placares[3]>placares[2])and (placares[0]==placares[1]or placares[3]==placares[2]):
                        return 4
                    elif(placares[0]==placares[1]or placares[3]==placares[2])and (placares[0]<placares[1]or placares[3]<placares[2]):
                        return 1
    
    pontos1=pontos_time1
        
    def pontos_time2(placares):
        if placares[1]>placares[0]and placares[2]>placares[3]:
            return 6
        elif placares[1]==placares[0]and placares[2]==placares[3]:
            return 2
        else:
            if placares[1]<placares[0]and placares[2]<placares[3]:
                return 0
            elif (placares[1]>placares[0]or placares[2]>placares[3])and (placares[1]<placares[0]or placares[2]<placares[3]):
                return 3
            else:
                if(placares[1]>placares[0]or placares[2]>placares[3])and (placares[1]==placares[0]or placares[2]==placares[3]):
                    return 4
                elif (placares[1]==placares[0]or placares[2]==placares[3])and (placares[1]<placares[0]or placares[2]<placares[3]):
                    return 1

    return {confronto1[0]:pontos_time1,confronto1[1]:pontos_time2}