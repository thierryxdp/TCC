def pontos_por_time(lista):
    '''
        Condição do primeiro jogo:
    if lista[0][2][0]>lista[0][2][1]:
        Cormengo = 3
        Flaminthians = 0
    elif lista[0][2][0]<lista[0][2][1]:
        Flaminthians = 3
        Cormengo = 0
    elif lista[0][2][0]==lista[0][2][1]:
        Flaminthians = 1
        Cormengo=1
        Condição do segundo jogo:
     if lista[1][2][0]>lista[1][2][1]:
        Cormengo2 = 3
        Flaminthians2 = 0
    elif lista[1][2][0]<lista[1][2][1]:
        Flaminthians2 = 3
        Cormengo2 = 0
    elif lista[1][2][0]==lista[1][2][1]:
        Flaminthians2 = 1
        Cormengo2 = 1
    PARAMETROS:
        total_Cormengo = int.
        total_Flaminthians = int.
        Cormengo = int.
        Flaminthians = int.
        Cormengo2 = int.
        Flaminthians2 = int.
        pontos = dict.
    '''
#Primeiro jogo
    if lista[0][2][0]>lista[0][2][1]:
        Cormengo = 3
        Flaminthians = 0
    elif lista[0][2][0]<lista[0][2][1]:
        Flaminthians = 3
        Cormengo = 0
    elif lista[0][2][0]==lista[0][2][1]:
        Flaminthians = 1
        Cormengo=1
#Segundo jogo
    if lista[1][2][0]>lista[1][2][1]:
        Cormengo2 = 3
        Flaminthians2 = 0
    elif lista[1][2][0]<lista[1][2][1]:
        Flaminthians2 = 3
        Cormengo2 = 0
    elif lista[1][2][0]==lista[1][2][1]:
        Flaminthians2 = 1
        Cormengo2 = 1
#Total de pontos
    total_Cormengo =  Cormengo + Cormengo2
    total_Flaminthians = Flaminthians + Flaminthians2 
    pontos={"Cormengo":total_Cormengo,"Flaminthians":total_Flaminthians}
    return pontos