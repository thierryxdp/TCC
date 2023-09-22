def pontos_por_time(lista):
	tabela = {lista[0][0]:0,lista[0][1]:0}
    if lista[0][2][0] > lista[0][2][1]:
		tabela[lista[0][0]] += 3
    elif lista[0][2][0] < lista[0][2][1]:
        tabela[lista[0][1]] += 3
    elif lista[0][2][0] = lista[0][2][1]:
        tabela[lista[0][0]] += 1
        tabela[lista[0][1]] += 1
    elif lista[1][2][1] > lista [1][2][0]:
        tabela[lista[0][0]] += 3
	elif lista[1][2][1] < lista [1][2][0]:
        tabela[lista[0][1]] += 3
	elif lista[1][2][1] = lista [1][2][0]:
        tabela[lista[0][0]] += 1
        tabela[lista[0][1]] += 1