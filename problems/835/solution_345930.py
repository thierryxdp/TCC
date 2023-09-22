def melhor_volta(matriz):
    """funcao que retorna o resultado do corredor com a volta com o menor tempo;
    list(list) -> tuple"""

    melhorTempo = 1000
    
     
    for i in range(len(matriz)):
        menorTempo = min(matriz[i])    
            
        if melhorTempo > menorTempo:
            
            melhorTempo = menorTempo
            corredor = i
            coluna = matriz[i].index(melhorTempo)

    return ((corredor+1),melhorTempo,coluna+1)