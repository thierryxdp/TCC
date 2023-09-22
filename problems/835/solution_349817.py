def melhor_volta(matriz):
    """Recebe uma matriz, com certos dados e retorna o melhor dado o contexto.
    list -> tuple"""
    
    menor = 0
    corredor = 0
    for i in range(0, len(matriz)):
        
        menortemp = min(matriz[i])
        
        if menortemp < menor or menor == 0:
            menor = menortemp
            
            corredor = 1 + i
            volta = 1 + matriz[i].index(menor)
     
    return (corredor, menor, volta)