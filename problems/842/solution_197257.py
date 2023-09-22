#Start your python function here
def pontos_por_time(x):
    """
    Calcula e retorna um dicionario com os times e os numeros de pontos
    a partir de uma lista com 2 elementos com as informacoes dos jogos;
    list -> dict
    """
    if x[0][0] == 'Cormengo' and x[0][2] > x[0][3] and x[1][0] == 'Cormengo' and x[1][2] > x[1][3]:
        return {'Cormengo':6,'Flamínthians':0}
    if x[0][0] == 'Cormengo' and x[0][2] > x[0][3] and x[1][0] == 'Flamínthians' and x[1][2] > x[1][3]:
        return {'Cormengo':3,'Flamínthians':0}
    if x[0][0] == 'Flamínthians' and x[0][2] > x[0][3] and x[1][0] == 'Cormengo' and x[1][2] > x[1][3]:
        return {'Cormengo':0,'Flamínthians':3}
    if x[0][0] == 'Flamínthians' and x[0][2] > x[0][3] and x[1][0] == 'Flamínthians' and x[1][2] > x[1][3]:
        return {'Cormengo':0,'Flamínthians':6}
    if x[0][0] == 'Cormengo' and x[0][2] > x[0][3] and x[1][2] == x[1][3]:
        return {'Cormengo':3,'Flamínthians':1}
    if x[0][0] == 'Flamínthians' and x[0][2] > x[0][3] and x[1][2] == x[1][3]:
        return {'Cormengo':1,'Flamínthians':3}
    if x[0][2] == x[0][3] and x[1][2] == x[1][3]:
        return {'Cormengo':1,'Flamínthians':1}