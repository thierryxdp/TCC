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
        return {'Cormengo': 2, 'Flamínthians': 2}