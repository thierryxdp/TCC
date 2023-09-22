def melhor_volta (matriz):
    '''função que dada uma matriz com tempos em segundos das voltas de cada corredor retorna de quem foi a melhor
    volta, com qual tempo e em que volta; list->tuple'''
 	melhorvolta =1000
    vencedor = 0
    for i in range(len(matriz)):
    	for j in range9len(matriz[0]):
            if matriz[i][j]<= melhorvolta:
                melhorvolta=matriz[i][j]
                vencedor=(i+1,matriz[i][j],j+1)
     
     return vencedor