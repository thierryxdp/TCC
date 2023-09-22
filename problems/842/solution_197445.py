def pontos_por_time(lista):
    """
    Função que recebe uma lista com o nome de dois times e com
    o placar deles em dois jogos. Com isso calcularemos o número
    de pontos de cada um e retornaremos um dicionário contendo o
    nome e seus pontos.
    Param lista: list
    Return: dict
    """

    numero_pontos_time11 = 0
    numero_pontos_time12 = 0
    numero_pontos_time21 = 0
    numero_pontos_time22 = 0
    

    jogo_ida = lista[0]
    time11 = jogo_ida[0]
    time12 = jogo_ida[1]
    
    primeiro_placar = lista[1]
    placar_time11 = primeiro_placar[0]
    placar_time12 = primeiro_placar[1] 

    if (placar_time11 > placar_time12):
        numero_pontos_time11 = numero_pontos_time11 +3
        numero_pontos_time12 = numero_pontos_time12 + 0
    elif (placar_time11 < placar_time12):
        numero_pontos_time11 = numero_pontos_time11 + 0
        numero_pontos_time12 = numero_pontos_time12 + 3
    else:
        numero_pontos_time11 = numero_pontos_time11 + 1
        numero_pontos_time12 = numero_pontos_time12 + 1

    
    jogo_volta = lista[2]
    time21 = jogo_volta[0]
    time22 = jogo_volta[1]
    
    segundo_placar = lista[3]
    placar_time21 = segundo_placar[0] 
    placar_time22 = segundo_placar[1]

    if (placar_time21 > placar_time22):
        numero_pontos_time21 = numero_pontos_time21 +3
        numero_pontos_time22 = numero_pontos_time22 + 0
    elif (placar_time21 < placar_time21):
        numero_pontos_time21 = numero_pontos_time21 + 0
        numero_pontos_time22 = numero_pontos_time22 + 3
    else:
        numero_pontos_time21 = numero_pontos_time21 + 1
        numero_pontos_time22 = numero_pontos_time22 + 1

    total_time1 = numero_pontos_time11 + numero_pontos_time21
    total_time2 = numero_pontos_time12 + numero_pontos_time22

    return {time11:total_time1,time12:total_time2}