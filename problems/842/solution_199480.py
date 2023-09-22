def pontos_por_time (lista1, lista2):
    '''Essa função recebe uma lista de dois elementos, onde cada um
    desses elementos  é também uma lista.list, list -> dict'''
    
    lista1=['time1','time2',[2, 1]]
    lista2 =['time2','time1', [2, 2]] 
    ida = lista1
    volta = lista2

    if ida[2][0] > ida[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 3
        
    if ida[2][0] == ida[2][1]:
        dicionario[ida[0]] = dicionario[ida[0]] + 1
        dicionario[ida[1]] = dicionario[ida[1]] + 1

    if ida[2][0] < ida[2][1]:
        dicionario[ida[1]] = dicionario[ida[1]] + 3

    if volta[2][0] > volta[2][1]:
        dicionario[volta[0]] = dicionario[volta[0]] + 3
        
    if volta[2][0] == volta[2][1]:
        dicionario[volta[0]] = dicionario[volta[0]] + 1
        dicionario[volta[1]] = dicionario[volta[1]] + 1

    if volta[2][0] < volta[2][1]:
        dicionario[volta[1]] = dicionario[volta[1]] + 3
        return dicionario