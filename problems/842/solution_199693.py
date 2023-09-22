def pontos_por_time(lista):
    '''funcao que recebe uma lista com dois elementos que sao listas que tem dados dos jogos de ida
    e volta entre dois times de futebol e retorna o numero de pontos do time na fase:
    entrada: lista; saida: dicionario'''
    pontos_cor = []
    pontos_fla = []
    if lista[0] == "Flamínthians":
    	if (lista[1])[0] > (lista[1])[1]
    	pontos_fla = [3,] and pontos_cor = [0,]
    	elif (lista[1])[0] < (lista[1])[1]
        pontos_fla = [0,] and pontos_cor = [3,]
        elif  (lista[1])[0] = (lista[1])[1]
        pontos_fla = [1,] and pontos_cor = [1,]
        if (lista[2])[0] > (lista[2])[1]
    	pontos_fla += [3,] and pontos_cor += [0,]
    	elif (lista[2])[0] < (lista[2])[1]
        pontos_fla += [0,] and pontos_cor += [3,]
        elif  (lista[2])[0] = (lista[2])[1]
        pontos_fla += [1,] and pontos_cor += [1,]
    else:
        	if (lista[1])[0] > (lista[1])[1]
    	pontos_fla = [3,] and pontos_cor = [0,]
    	elif (lista[1])[0] < (lista[1])[1]
        pontos_fla = [0,] and pontos_cor = [3,]
        elif  (lista[1])[0] = (lista[1])[1]
        pontos_fla = [1,] and pontos_cor = [1,]
        if (lista[2])[0] > (lista[2])[1]
    	pontos_fla += [3,] and pontos_cor += [0,]
    	elif (lista[2])[0] < (lista[2])[1]
        pontos_fla += [0,] and pontos_cor += [3,]
        elif  (lista[2])[0] = (lista[2])[1]
        pontos_fla += [1,] and pontos_cor += [1,]
    
    return {'Cormengo': pontos_cor, 'Flaminthias': pontos_fla}