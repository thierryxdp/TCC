def pontos_por_time(lista):
    '''Função que dada uma lista contendo duas listas com informações a respeito
    de dois jogos entre dois times(ida e volta) no seguinte esquema:
    [['time1', 'time2', [gols_time1, gols_time2]], ['time2', 'time1',[gols_time2, gols_time1]]]
    retornará um dicionario contendo o nome do time e o total de pontos feitos nessas duas rodadas.
    param -> list[list,list]
    return -> dict'''
    
    ida, volta = lista[0], lista[1]
    dicionario = {ida[0]: 0, ida[1]: 0}
    
    if ida[2][0] > ida[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 3
    if ida[2][0] == ida[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 1
        dicionario[ida[1]] = dicionario[ida[1]] + 1
    
    if volta[2][0] > volta[2][1]:
        dicionario[ida[1]] = dicionario[ida[1] + 3
                                        
    if volta[2][0] == volta[2][1]:
        dicionario[ida[1]] = dicionario[ida[1]] + 1 
        dicionario[ida[0]] = dicionario[ida[0]] + 1
        
    return dicionario