def pontos_por_time(lista):
    """ Função que recebe uma lista com duas listas, 
    com os times e os gols de ida e volta e retorna 
    a pontuação total da fase. list -> dict """
    time1= lista[0][0]
    time2= lista[0][1]
    gols_ida_time1 = lista[0][2][0]
    gols_ida_time2 = lista[0][2][1]
    gols_volta_time1 = lista[1][2][0]
    gols_volta_time2 = lista[1][2][1]
    
    
    acum1 = 0
    acum2 = 0

    if gols_ida_time1 > gols_ida_time2:
        acum1 += 3
        

    elif gols_ida_time1 == gols_ida_time2:
        acum1 +=1
        acum2 +=1
        

    elif gols_ida_time1 < gols_ida_time2:
        acum2 +=3
        
                
    if gols_volta_time1 > gols_volta_time2:
        acum1 +=3
        
        
    elif gols_volta_time1 == gols_volta_time2:
        acum1 +=1
        acum2 +=1   
        
    elif gols_volta_time1 < gols_volta_time2:
        acum2 +=3 

    pontos = [(time1, acum1),(time2, acum2)]
        

    pontos_dic = dict(pontos)
        
    return pontos_dic