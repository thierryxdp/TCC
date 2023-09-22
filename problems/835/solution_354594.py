def melhor_volta(matriz):
    """Recebe matriz com o tempo e volta de cada corredor
    e retorna qual foi o menor tempo;
    list[???][???] --> int"""
    
    menor_Volta = 100000
    corredor_Campeao = ()

    for corredor in range(len(matriz)):
        for tempo in range(len(matriz[corredor])): 
            if menor_Volta > matriz[corredor][tempo]:
                corredor_Campeao += (corredor,)
                menor_Volta = matriz[corredor][tempo]

    return corredor_Campeao