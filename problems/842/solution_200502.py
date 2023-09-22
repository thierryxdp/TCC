def pontos_por_time(lista):
    '''
    recebe uma lista com dois elementos que também são listas e retorna um dicionário
    lista -> dicionario
    '''
    ida = lista[0]
    volta = lista[1]
    gols_ida = ida[2]
    gols_volta = volta[2]
    if gols_ida[0] == gols_ida[1] and gols_volta[0] == gols_volta[1]:
        return {ida[0]: 2, ida[1]: 2}
    elif gols_ida[0] == gols_ida[1] and gols_volta[1] > gols_volta[0]:
        return {ida[0]: 4, ida[1]: 1}
    elif gols_ida[0] == gols_ida[1] and gols_volta[1] < gols_volta[0]:
        return {ida[0]: 1, ida[1]: 4}
    elif gols_volta[0] == gols_volta[1] and gols_ida[1] > gols_ida[0]:
        return {ida[0]: 4, ida[1]: 1}
    elif gols_volta[0] == gols_volta[1] and gols_ida[1] < gols_ida[0]:
        return {ida[0]: 1, ida[1]: 4}
    elif gols_ida[0] > gols_ida[1] and gols_volta[1] > gols_volta[0]:
        return {ida[0]: 6, ida[1]: 0}
    elif gols_ida[0] < gols_ida[1] and gols_volta[1] < gols_volta[0]:
        return {ida[0]: 0, ida[1]: 6}
    else: 
        return {ida[0]: 3, ida[1]: 3}