#Start your python function here
def pontos_por_time(lista):
    '''Essa função informa dois times, e os seus respectivos pontos acumulados, em dois jogos
    lista -> dicionário'''
    p1=0
    p2=0
    if lista[0][2][0] > lista[0][2][1]:
        p1=p1+3
    elif lista[0][2][0] < lista[0][2][1]:
        p2=p2+3
    if lista[1][2][0] > lista[1][2][1]:
        p2=p2+3
    elif lista[1][2][0] < lista[1][2][1]:
        p1=p1+3
    else:
        p1=p1+1
        p2=p2+1
    return {lista[0][0]:p1 , lista[0][1]:p1}