def pontos_por_time(lista):
    '''Receber uma lista com informacoes sobre dois jogos (ida e volta) entre dois times,
    retorna um dicionário cujos mapeamentos são: <nome do time> → <numero de pontos na fase>;
    list -> dictionary'''
	time_a = 0
    time_b = 0

    if lista[0][2][0] > lista[0][2][1]:
        time_a += 3

    elif lista[0][2][0] < lista[0][2][1]:
        time_b += 3
    
    else:
        time_a += 1
        time_b += 1

    if lista[1][2][0] > lista[1][2][1]:
        time_b += 3

    elif lista[1][2][0] < lista[1][2][1]:
        time_a += 3
    
    else:
        time_a += 1 
        time_b += 1

    return {lista[0][0]: time_a, lista[0][1]: time_b}ur python function here