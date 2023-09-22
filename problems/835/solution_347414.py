def melhor_volta(matriz):
    """Mostra de quem foi a melhor volta da prova, o tempo e a respectiva volta
    	list -> tuple
        Parameters:
        matriz: Matriz com os tempos, em segundos, dos corredores
        
        Returns:
        A melhor volta da prova, o tempo e a respectiva volta
    """
    
    tempo = []
    for i in range(len(matriz)):
        tempo.append(min(matriz[i]))
        menor = min(tempo)
        
        if menor in matriz[i]:
            vencedor = matriz.index(matriz[i]) + 1
            volta = matriz[i].index(min(tempo)) + 1
            
    return (vencedor, tempo, volta)