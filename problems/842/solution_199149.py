def pontos_por_time(lista):
    '''Funcao que receba uma lista de dois elementos,
       onde cada elemento é também uma lista, e 
       retorne um dicionario com o nome do time
       e numero total de pontos na fase
       list -> dict
    '''
    if lista[0]>lista[1]:
       return lista[0]
    if 'time2'>'time1':
       return lista[1]
    if 'time1'=='time2':
       return 'empate'