# Recebe uma lista com as três dimensões do colchão, em centímetros, ordenadas da menor para a
#maior e dois inteiros H e L, respectivamente altura e largura da porta de João e retorna um 
#booleano indicando se o colchão passa ou não pela porta
#medidas: lista com as dimensões do colchão; 
#H:Altura da porta; L: Largura da Porta
def colchao(medidas,H,L):
	if medidas[1] or medidas[2]< H:
        return True
    else:
        return False