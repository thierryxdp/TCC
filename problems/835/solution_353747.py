def melhor_volta (matriz):
    '''função que dada uma matriz com tempos em segundos das voltas de cada corredor retorna de quem foi a melhor
    volta, com qual tempo e em que volta; list->tuple'''
 	tupla = (0,float('inf'),0)
 	for i in range(5):
        for j in range(9):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1) 

 return tupla