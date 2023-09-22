def pontos_por_time(lista):
    '''Funcao que receba uma lista de dois elementos,
       onde cada elemento é também uma lista, e 
       retorne um dicionario com o nome do time
       e numero total de pontos na fase
       list -> dict
    '''
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
       return {lista[0][0]:6, lista[0][1]:0}
    elif lista[0][2][0] == lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
       return {lista[0][0]:2, lista[0][1]:2}
    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
       return {lista[0][0]:0, lista[0][1]:6}
    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
       return {lista[0][0]:3, lista[0][1]:3}
    else:
       return {lista[0][0]:1, lista[0][1]:4}