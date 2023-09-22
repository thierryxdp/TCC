def pontos_por_time(info):
    dicionario = {}
    dicionario[info[0][0]] = 0
    dicionario[info[0][1]] = 0
    
    if info[0][2][0] == info[0][2][1]:
        dicionario[info[0][0]] += 1 
        dicionario[info[0][1]] += 1
    elif info[1][2][0] == info[1][2][1]:
        dicionario[info[0][0]] += 1 
        dicionario[info[0][1]] += 1
    elif info[0][2][0] >= info[0][2][1]:
        dicionario[info[0][0]] += 3
        dicionario[info[1][0]] += 3
    elif info[1][2][0] >= info[1][2][1]:
        dicionario[info[0][0]] += 3
        dicionario[info[0][1]] += 3
    else:
        dicionario[info[0][1]] += 3
        dicionario[info[1][1]] += 3
    return dicionario