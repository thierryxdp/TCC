#Start your python function here
def pontos_por_time (jogo_ida, jogo_volta):
    '''Recebe as informações, como o nome dos dois times e o placar, dos jogos de ida e volta.
       list, list -> list'''
    timeA = jogo_ida[0]
    timeB = jogo_ida[1]
    pontos_timeA = jogo_ida[2[0]] + jogo_volta[2[1]]
    pontos_timeB = jogo_ida[2[1]] + jogo_volta[2[0]]
    resultado = (timeA, pontos_timeA, timeB, pontos_timeB)
    return resultado