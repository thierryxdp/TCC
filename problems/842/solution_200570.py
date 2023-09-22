def pontos_por_time(tabela):

    ''' A função recebe uma tabela de campeonato no formato dicionário e retorna uma lista com:
        uma sublista da tabela, a média de pontos por time e o total de pontos do time campeão;
        dicionario --> lista
    '''

    pontos = list(dict.values(tabela))

    time = list(dict.keys(tabela))

    tabela_campeonato = list(dict.items(tabela))
        
    media_pontos = sum(pontos)/len(time)

    campeao = max(pontos)

    
    return [tabela_campeonato , media_pontos , campeao]