#Start your python function here
def pontos_por_time(fase):
    '''Dada uma lista de listas contendo o número de gols de dois jogos entre dois times, retorna um dicionnário com os pontos calculados de cada time na rodada
    list[list[str,str,list[int,int]],list[str,str,list[int,int]]] -> dict'''
    
    ida = fase[0]
    volta = fase[1]	    
    time1 = 0
    time2 = 0
    pontos = {}
    
    #Resultado jogo de ida
    if ida[2][0] > ida[2][1]: 
        time1 += 3
    if ida[2][0] < ida[2][1]:
        time2 += 3
    if ida[2][0] == ida[2][1]:
        time1 += 1
        time2 += 1
        
    #Resultado jogo de volta    
    if volta[2][0] > volta[2][1]: 
        time2 += 3
    if volta[2][0] < volta[2][1]:
        time1 += 3
    if volta[2][0] == volta[2][1]:
        time2 += 1
        time1 += 1
    
    #Criando chaves e atribuindo seus valores
    pontos[fase[1][0]] = time1
    pontos[fase[1][1]] = time2

    return pontos