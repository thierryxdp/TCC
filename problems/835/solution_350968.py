def melhor_volta(matriz):
    """
    	Função que retorna de quem foi a melhor volta, com
        qual tempo e em que volta.
        Matriz = 6(corredores) por 10(voltas)
    	list(list) -> tupla
	"""
    from random import randint
	menor = 0
	matriz = []
	tamanho = 4
	posicoes = []
	for i in range(tamanho):
   	 	linha = []
    	for j in range(tamanho):
       		n = randint(1, 10)
        	if n > maior: 
            	posicoes = [(i, j)]
            	maior = n
        	elif n == maior: 
           		posicoes.append((i, j))
        		linha.append(n)

    matriz.append(linha)
    return matriz