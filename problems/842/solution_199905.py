#Start your python function here
def pontos_por_time(jogostimes):
    jogo1=x[0]
    jogo2=x[1]
    jogostimes=[jogo1,jogo2]
    x=jogo1[2]
    y=jogo2[2]
    if x[0] > x[1] and y[1] > y[0]:
        return {jogo1[0]: 0, jogo1[1]: 6}
    elif x[0] < x[1] and y[1] < y[0]:
        return {jogo1[0]: 6, jogo1[1]: 0}
    elif x[0] == x[1] and y[0] == y[1]:
        return {jogo1[0]: 2, jogo1[1]: 2}
    elif x[0] > x[1] and y[1] < y[0]:
        return {jogo1[0]: 3, jogo1[1]: 3}
    elif x[0] < x[1] and y[1] > y[0]:
        return {jogo1[0]: 3, jogo1[1]: 3}
    elif x[0] > x[1] and y[0] == y[1]:
        return {jogo1[0]: 1, jogo1[1]: 4}
    elif x[1] > x[0] and y[0] == y[1]:
        return {jogo1[0]: 4, jogo1[1]: 1}
    elif x[0] == x[1] and y[1] > y[0]:
        return {jogo1[0]: 1, jogo1[1]: 4}
    elif x[0] == x[1] and y[0] > y[1]:
        return {jogo1[0]: 4, jogo1[1]: 1}