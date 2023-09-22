def melhor_volta(matriz):
    '''
    Funçao que recebe as 10 voltas que cada corredor fez
    e diz quem fez a menor volta, em quanto tempo e em qual 
    volta foi
    list -> tuple
    '''
    resposta=(0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<resposta[1]:
            	resposta=(i+1,matriz[i][j],j+1)
	return resposta