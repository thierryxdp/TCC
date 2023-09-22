def pontos_por_time(lista):
    ''' Função que recebe uma lista de entrada contendo informações sobre o jogo
    de duas equipes de futebol e retorna um dicionário contendo informações sobre
    suas respectivas pontuações. list -> dict'''
    pontos1 = 0
    #Vitoria para o time 1
    
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][0] < lista[1][2][1]:
        return {str(lista[0][0]): 6, str(lista[0][1]): 0}
    elif lista[0][2][0] > lista[0][2][1] and lista[1][2][0] == lista[1][2][1]:
        return  {str(lista[0][0]): 4, str(lista[0][1]): 1}
    elif lista[0][2][0] == lista[0][2][1] and lista[1][2][0] < lista[1][2][1]:
        return  {str(lista[0][0]): 4, str(lista[0][1]): 1}

    #Empate
    elif lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return {str(lista[0][0]): 2, str(lista[0][1]): 2}

    elif lista[0][2][0] >  lista[0][2][1] and lista[1][2][0] > lista[1][2][1]:
        return {str(lista[0][0]): 3, str(lista[0][1]): 3}
    
    elif lista[0][2][0] <  lista[0][2][1] and lista[1][2][0] < lista[1][2][1]:
        return {str(lista[0][0]): 3, str(lista[0][1]): 3}
    #vitoria para o time 2

    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][0] > lista[1][2][1]:
        return {str(lista[0][0]): 0, str(lista[0][1]): 6}
    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][0] == lista[1][2][1]:
        return  {str(lista[0][0]): 1, str(lista[0][1]): 4}
    elif lista[0][2][0] == lista[0][2][1] and lista[1][2][0] > lista[1][2][1]:
        return  {str(lista[0][0]): 1, str(lista[0][1]): 4}