def posLetra(stringue,letra,numero):
	"""retorna a posicao da string q a ocorrencia da letra ta, caso
    exita menos ocorrencias retorna -1"""
    contador = 0
    resposta = 0
    
    if numero == 1: ## n = 1 primeira resposta
        return str.find(stringue,letra)
    
    if str.count(stringue,letra)<numero: ## n maior = -1
        return -1
    
    ##casos separados
    while resposta<numero:
    	if str.count(stringue,letra)>numero:
    		resposta = str.find(stringue,letra,resposta+1, -1)
    
    	if str.count(stringue,letra) == numero:
       		resposta = str.find(stringue,letra,resposta+1, -1)
	return resposta