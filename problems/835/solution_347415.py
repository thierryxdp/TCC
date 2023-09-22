def melhor_volta(matriz):
    """Mostra de quem foi a melhor volta da prova, o tempo e a respectiva volta
    	list -> tuple
        Parameters:
        matriz: Matriz com os tempos, em segundos, dos corredores
        
        Returns:
        A melhor volta da prova, o tempo e a respectiva volta
    """
    
    menos = []
    for i in range(len(matriz)):
        menos.append(min(matriz[i]))
        menor = min(menos)
        
        if menor in matriz[i]:
            quem = matriz.index(matriz[i])+1
            qual = matriz[i].index(min(menos))+1
            
    return (quem, menor, qual)