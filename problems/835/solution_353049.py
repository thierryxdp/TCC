def melhor_volta(matriz_tempos):
    #Essa funcao faz uma varedura dos itens de uma matrix 6x10 que corresponde
    #aos tempos de uma corrida de kart, onde cada corredor correu 10 vezes
    #ela retorna uma tupla contendo o numero do corredor com melhor temop
    #quanto foi esse tempo e em qual volta
    #
 	tupla = (0,float(),0)
 	for i in range(6):
   		for j in range(10):
     		if matriz_tempos[i][j] < tupla[1]:
       			tupla = (i+1,matriz_tempos[i][j],j+1) 
 	return tupla