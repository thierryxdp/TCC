def melhor_volta(matriz):
    '''Função que recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta4
    list->tuple'''
tupla = (0,float(),0)
for i in range(6):
	for j in range(10):
	    if matriz[i][j] < tupla[1]:
			tupla = (i+1,matriz[i][j],j+1)
				return tupla