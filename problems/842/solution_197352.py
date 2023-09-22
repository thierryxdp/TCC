def pontos_por_time(lista):
    '''
    	Função que recebe uma lista com dois
        elementos, sendo cada um uma lista
        com os times e seus respectivos 
        números de gols em cada jogo, e
        retorna um dicionário cujas chaves
        são o nome dos times e cujos valores 
        são o número total de pontos do time
        na fase
        : param lista:list
        : return: dict
    '''
    
    if (lista[0][2][0] > lista[0][2][1]) and (lista[1][2][0] > lista[1][2][1]):
        return {lista[0][0]: 6, lista[0][1]: 0}
    
    elif ((lista[0][2][0] > lista[0][2][1]) and (lista[1][2][0] == lista[1][2][1])) or ((lista[0][2][0] == lista[0][2][1]) and (lista[1][2][0] > lista[1][2][1])):
        return {lista[0][0]: 4, lista[0][1]: 1}
    
    elif (lista[0][2][0] < lista[0][2][1]) and (lista[1][2][0] < lista[1][2][1]):
        return {lista[0][0]: 0, lista[0][1]: 6}
    
    elif (lista[0][2][0] == lista[0][2][1]) and (lista[1][2][0] == lista[1][2][1]):
        return {lista[0][0]: 1, lista[0][1]: 1}
    
    elif ((lista[0][2][0] < lista[0][2][1]) and (lista[1][2][0] == lista[1][2][1])) or ((lista[0][2][0] == lista[0][2][1]) and (lista[1][2][0] < lista[1][2][1])):
        return {lista[0][0]: 1, lista[0][1]: 4}
    
    else:
        return {lista[0][0]: 3, lista[0][1]: 3}