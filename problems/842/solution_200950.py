def pontos_por_time(fase):
    """Essa função recebe como parâmetro de entrada uma lista de dois elementos em que cada um também é uma lista e retorna um dicionário com o nome do time e o número total de pontos da fase
    list->dict"""
 ida = fase[0]
 volta = fase[1]
 nome_time_1 = ida[0]
 nome_time_2 = ida[1]
 dic = {nome_time_1: 0, nome_time_2: 0}
	if ida[2][0] > ida[2][1]:
    	dic[nome_time_1] += 3
	elif ida[2][0] == ida[2][1]:
   		dic[nome_time_1] += 1
    	dic[nome_time_2] += 1
	else:
    	dic[nome_time_2] += 3
	if volta[2][0] > volta[2][1]:
    	dic[nome_time_2] += 3
	elif volta[2][0] == volta[2][1]:
    	dic[nome_time_1] += 1
    	dic[nome_time_2] += 1
	else:
    	dic[nome_time_1] += 3
	return dic