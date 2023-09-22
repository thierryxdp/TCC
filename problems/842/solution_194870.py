def pontos_por_time(lista):
    '''funcao que recebe como entrada duas listas, denominadas lista1 e lista2, que contem informacoes e de volta, respecti 
    do numero de gols nos jogos de ida e de volta, respectivamente e retorna um dicionario que mapeia
    o numero de pontos de um time na fase
    list -> dicionario'''
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return {lista[0][0]:6, lista[0][1]:0}
    elif lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1] or lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return {lista[0][0]:3, lista[0][1]:3}
    elif lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1] or lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]: 
        return {lista[0][0]:4, lista[0][1]:1}
    elif lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return {lista[0][0]:0, lista[0][1]:6}
    elif lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1] or lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return {lista[0][0]:1, lista[0][1]:4}
    else:
    	return {lista[0][0]:2, lista[0][1]:2}