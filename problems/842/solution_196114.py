#Start your python function here
def pontos_por_time(lista):
    lista1 = lista[0]
    lista2 = lista[1]
    result = {}
    gols1 = lista1[2][0] + lista2[2][1]
    gols2 = lista1[2][1] + lista2[2][0]
    pntTime1 = 0
    pntTime2 = 0
    if(lista1[0] == lista2[1] and lista1[1] == lista2[0]):
        #partida1
        if(lista1[2][0] > lista1[2][1]):
            pntTime1 += 3
        elif(lista1[2][0] == lista1[2][1]):
            pntTime1 += 1
            pntTime2 += 1
        else:
            pntTime2 += 3
        #partida2
        if(lista2[2][0] > lista2[2][1]):
            pntTime2 += 3
        elif(lista2[2][0] == lista2[2][1]):
            pntTime1 += 1
            pntTime2 += 1
        else:
            pntTime1 += 3
        if( gols1 > gols2):
            result[lista1[0]]= pntTime1
            result[lista1[1]]= pntTime2
        elif( gols1 == gols2):
            result[lista1[0]]= pntTime1
            result[lista1[1]]= pntTime2
        else:    
            result[lista1[1]]= pntTime2
            result[lista1[0]]= pntTime1
        return result
    else:
        return "Times não conferem"