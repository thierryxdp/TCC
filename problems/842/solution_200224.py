def pontos_por_time(lista=[]):
    '''Dados os elemetnos da lista, retorna um dicionário com os pontos de cada time'''
    jogo_ida=lista[0]
    jogo_volta=lista[1]
    time1=jogo_ida[0]
    time2=jogo_ida[1]
    placar_ida=jogo_ida[2]
    placar_volta=jogo_volta[2]
    ponto1=(placar_ida[0])+(placar_volta[1])
    ponto2=(placar_ida[1])+(placar_volta[0])
    return {jogo_ida[0]:(ponto1), jogo_ida[1]:(ponto2)}