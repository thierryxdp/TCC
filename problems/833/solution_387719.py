def conta_numero(numero, matriz):
    ''' funçao que ao dar um numero inteiro e uma matriz
    	determina quantas vezes este numero inteiro se
        repetiu dentro dessa matriz.
        int, list(list) ---> int '''
    linhas = len(matriz)
    colunas = len(matriz[0])
    a = 0
    b = 0
    qtdrepeticoes = 0
    for a in range(0, linhas):
		if numero in matriz[a]:
        	qtdrepeticoes = qtdrepeticoes + list.count(matriz[a],numero)
        			return qtdrepeticoes
        else:
            return 0