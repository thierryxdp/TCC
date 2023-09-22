def posLetra(stringue,letra,n):
	contador = 0
    resposta = []
    
    if n == 1: ###primeira ocorrência
    	return str.find(stringue,letra)

    elif n <= str.count(stringue,letra):
        while contador<len(stringue):
            if stringue[contador] in letra:
                list.append(resposta,contador)
                contador+=1
        return resposta[n-1]
    elif n > str.count(stringue,letra): ### menos ocorrências da letra do que a ocorrência pedida
        return -1