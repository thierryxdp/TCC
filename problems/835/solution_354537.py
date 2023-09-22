def melhor_volta(matriz):
    '''funcao que recebe os tempos dos pilotos em cada volta e retorna uma tupla que informa o responsavel pela melhor volta com o tempo  obtido e em qual volta ele atingiu a marca list -> tuple'''
    tempoMinimo = []
    
    for i in matriz:
        
        tmpmin = min(i)
        
    list.append(tempoMinimo,tmpmin)
    
    tempo = min(tempoMinimo)
    
    piloto = list.index(tempoMinimo,a) + 1
    
    for i in range(len(matriz)):
       
    	for volta in range(len(matriz[i])):
            
            if tempo == matriz[i][b]:
                
                volta = b + 1 
                
                
    return (piloto,tempo,volta)