def pontos_por_time(lista):
    """função que recebe uma lista com o placar de dois jogos de futebol de dois times e retorna um dicionário com os times relacionados aos pontos que cada um fez. Vitória 3 pontos / empate 1 ponto"""
    time1 = lista[0][0]
    time2 = lista[0][1]
    placar = {time1:0,time2:0}
    if lista[0][2][0] > lista[0][2][1]:
        placar[time1] = 3
        return placar[time1]
    if lista[0][2][0] < lista[0][2][1]:
        return placar[time2] = 3
    if lista[0][2][0] == lista[0][2][1]:
        return placar[time1] = 1 and placar[time2] = 1
    if lista[1][2][0] > lista[1][2][1]:
        return placar[time1] =+ 3
    if lista[1][2][0] < lista[1][2][1]:
        return placar[time2] =+ 3
    if lista[1][2][0] == lista[1][2][1]:
        return placar[time1] =+ 1 and placar[time2] =+ 1
    return placar