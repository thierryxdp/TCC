def melhor_volta(matriz):
    '''Dada como entrada uma matriz 6x10 com
    os tempos em segundos dos corredores em 
    cada volta, retorna uma tupla informando 
    quem foi a melhor volta da prova, qual 
    o tempo e em que volta
    list -> tuple'''
    lista = []
    quem = 0
    contador = 0
    for linha in matriz:
        for coluna in linha:
			lista.append(coluna)
	melhor_tempo = min(lista)
    i = lista.index(melhor_tempo) + 1
    lista2 = [11,21,31,41,51,61]
    while contador < 1:
    	for a in lista2:
			if i < a:
				quem = lista2.index(a) + 1
                contador += 1
	return (quem, melhor_tempo)