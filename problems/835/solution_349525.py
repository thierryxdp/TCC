def melhor_volta(matriz:list) -> tuple:
    """comentário"""
    
    corredores = []
    tempos = []
    
    for i in range(len(matriz)):
        #Guardando os melhores tempos de cada corredor
        tempos.append(min(matriz[i]))
        
        #Definindo a melhor volta
        volta = matriz[i].index(min(matriz[i])) + 1
        
        #Guardando as informações da melhor volta de cada corredor
        corredores.append((i+1, min(matriz[i]), volta))
   
    #Definindo o menor tempo e a melhor volta dentre todas
    melhor_volta = corredores[tempos.index(min(tempos))]
    
    return melhor_volta