def melhor_volta(matriz):
    """funcao que retorna o resultado do corredor com a volta com o menor tempo;
    list(list) -> tuple"""

    volta = 1000
    
     
    for i in range(len(matriz)):
        menorTempo = min(matriz[i])    
            
        if volta > menorTempo:
            
            volta = menorTempo
            corredor = i
            coluna = matriz[i].index(menorTempo)

    return ((corredor+1),resultado,coluna+1)