#Start your python function here
def pontos_por_time (lista):
    '''Essa função recebe uma lista de dois elementos, onde cada um
    desses elementos  é também uma lista.list, list -> dict'''

    lista=[['time1','time2',[2, 1]], ['time2','time1', [2, 2]]] 

    ida = lista[0]
    volta = lista[1]
    dicionario = {ida[0]:0,ida[1]:0}

    if ida[2][0] > ida[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 3
        
    if ida[2][0] == ida[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 1
        dicionario[ida[1]] = dicionario[ida[1]] + 1

    if ida[2][0] < ida[2][1]:
        dicionario[ida[1]] = dicionario[ida[1]] + 3

    if volta[2][0] > volta[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 3
        
    if volta[2][0] == volta[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 1
        dicionario[ida[1]] = dicionario[ida[1]] + 1

    if volta[2][0] < volta[2][1]:
        dicionario[ida[1]] = dicionario[ida[1]] + 3
        return dicionario