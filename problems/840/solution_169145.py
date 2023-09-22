def bolos(xicaras_farinha,ovos,colheres_sopa):
	'''
calcula e retorna a quantidade de bolos que dara para
fazer dada a quantidade de ingredientes disponives
como entrada
float,float,float -> int 
	'''
    return min(xicaras_farinha//2,ovos//3,colheres_sopa//5)