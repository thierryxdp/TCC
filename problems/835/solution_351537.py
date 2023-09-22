def melhor_volta(matriz):
    '''Fazer uma funcao que receba uma matriz 6X10 e retorne uma tupla informando a melhor volta da prova, o seu tempo e em qual volta ela ocorreu;
    list -> tuple'''
    
    tempo_por_min = []
    volta = []
    
    for linha in matriz:
        tempo_por_min = tempo_por_min + [min(linha),]
        
    menortempo = min(tempo_por_min)
    corredor = list.index(tempo_por_min, menortempo) + 1
    
    for lista in matriz:
        for coluna in lista:
            if coluna == menortempo:
                melhor_volta = list.index(i,j) + 1
                
    return(corredor, menortempo, melhor_volta)