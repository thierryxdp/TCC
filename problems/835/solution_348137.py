def melhor_volta(matriz):
    '''
    Funcao que tem como entrada uma matriz que 6x10 que
    representa o numero de corredores e o numero de voltar
    respectivamente com os elementos representando os tempos
    das voltar. A funcao tem como retorno uma tupla contendo
    de qual corredor foi o menor tempo e em qual volta.
    	Parametros:
        	entrada:
            	matriz : list
            saida:
            	tuple
    '''
     tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return tupla