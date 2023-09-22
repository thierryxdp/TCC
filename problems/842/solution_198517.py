def pontos_por_time(lista):
    '''Função que dada uma lista contendo duas listas com informações a respeito
    de dois jogos entre dois times(ida e volta) no seguinte esquema:
    [['time1', 'time2', [gols_time1, gols_time2]], ['time2', 'time1',[gols_time2, gols_time1]]]
    retornará um dicionario contendo o nome do time e o total de pontos feitos nessas duas rodadas.
    param -> list[list,list]
    return -> dict'''
    
    ida, volta = lista[0], lista[1]
    dicionario = {'Cormengo': 0, 'Flaminthians': 0}
    
    if ida[2][0] > ida[2][1]:
        dicionario['Cormengo'] = dicionario['Cormengo'] + 3
    if ida[2][0] == ida[2][1]:
        dicionario['Cormengo'] = dicionario['Cormengo'] +1 and dicionario['Flaminthians'] = dicionario['Flaminthians'] + 1
    
    if volta[2][0] > volta[2][1]:
        dicionario['Flaminthians'] = dicionario['Flaminthians'] + 3
    if volta[2][0] == volta[2][1]:
        dicionario['Flaminthians'] = dicionario['Flaminthians'] + 1 and dicionario['Cormengo'] = dicionario['Cormengo'] + 1
        
    return dicionario