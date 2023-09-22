def melhor_volta(matriz):
	'''Dada uma matriz onde i representa os corredores 
    e j seus respectivos tempos 
    	list -> tup'''
	tempos = []
	for i in matriz:
		for j in i:
			tempos += [j]
	tempo = min(tempos)
	indice = tempos.index(tempo)
	quem = (indice // 10) + 1
	volta = (indice % 10) + 1
	return (quem, tempo, volta)