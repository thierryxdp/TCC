def melhor_volta(matriz):
    """funcao que retorna o resultado do corredor com a volta com o menor tempo;
    list(list) -> tuple"""

    resultado = 1000
    
     
    for i in range(len(matriz)):
        menor = min(matriz[i])    
            
        if resultado > menor:
             = menor
            corredor = i
            coluna = matriz[i].index(menor)

    return ((corredor+1),resultado,coluna+1)