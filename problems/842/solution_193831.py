def pontos_por_time(time1,time2,resultado1,resultado2):
    """função que retorna um dicionario com o nome do time e seu respectiva pontuação nos jogos
    list -> dicionario"""
    return {time1:resultado1 + resultado2, time2:resultado1 + resultado2}