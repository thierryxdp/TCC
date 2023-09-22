def pontos_por_time(lista1,lista2):
    '''funcao que recebe como entrada duas listas, denominadas lista1 e lista2, que contem informacoes e de volta, respecti 
    do numero de gols nos jogos de ida e de volta, respectivamente e retorna um dicionario que mapeia
    o numero de pontos de um time na fase
    list, list -> dicionario'''
    if lista1[2][0]>lista1[2][1] and lista2[2][0]<lista2[2][1]:
	    return {lista1[0]:6,lista1[1]:0}
    elif lista1[2][0]>lista1[2][1] and lista2[2][0]==lista2[2][1]:
	    return {lista1[0]:4,lista1[1]:1}
    elif lista1[2][0]>lista1[2][1] and lista2[2][0]>lista2[2][1] or lista1[2][0]<lista1[2][1] and lista2[2][0]<lista2[2][1]:
	    return {lista1[0]:3,lista1[1]:3}
    elif lista1[2][0]<lista1[2][1] and lista2[2][0]>lista2[2][1]:
	    return {lista1[1]:0,lista1[1]:6}
    elif lista1[2][0]<lista1[2][1] and lista2[2][0]==lista2[2][1]:
	    return {lista1[0]:1,lista1[1]:4}
    else:
	    return {lista1[0]:2,lista1[1]:2}