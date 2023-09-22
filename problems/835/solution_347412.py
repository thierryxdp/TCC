def melhor_volta(matriz):
    """Mostra de quem foi a melhor volta da prova, o tempo e a respectiva volta
    	list -> tuple
        Parameters:
        matriz: Matriz com os tempos, em segundos, dos corredores
        
        Returns:
        A melhor volta da prova, o tempo e a respectiva volta
    """
    
    tempo = volta = vencedor = 1000
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if min(matriz[i][j], tempo) == matriz[i][j]:
                tempo = min(matriz[i][j], tempo)
                vencedor = vencedor + 1
                volta = j + 1
                
    	return (vencedor, tempo, volta)