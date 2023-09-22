def repetidos(num):
    list.sort(num)
    n = 0
    resposta = 0
    while n+1 < len (num):
        if num[n]==num[n+1]:
        	resposta += 1
		n += 1
	return resposta