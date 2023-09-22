def soma_h(x):
    """Função que dado um número inteiro, retorna o resultado de um 1/x!"""
    """int--->float"""
    resposta=0
    for d in range(1,x+1):
        resposta+=1/d
 	return round(resposta,2)