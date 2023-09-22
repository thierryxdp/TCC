def melhor_volta(matriz):
    '''
    	Dada uma matriz com os tempos de cada um dos seis 
        corredores em cada uma das dez voltas a função 
        retorna uma tupla que diz qual foi a melhor volta,
        qual o tempo e em que volta foi.
        list -> tuple
    '''
    resultado = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < resultado[1]:
                resultado = (i+1, matriz[i][j], j+1)
    return resultado