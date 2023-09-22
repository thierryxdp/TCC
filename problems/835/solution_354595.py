def melhor_volta(matriz):
    """Recebe matriz com o tempo e volta de cada corredor
    e retorna qual foi o menor tempo;
    list[???][???] --> int"""
    
    tempo_menor = 999
    corredor_Campeao = ()
    volta_menor = 0

    for corredor in range(len(matriz)):
        for tempo in range(len(matriz[corredor])): 

            # Caso encontre a menor volta
            if menor_Volta > matriz[corredor][tempo]:
                corredor_Campeao = corredor
                tempo_menor = matriz[corredor][tempo]
                volta_menor = tempo

    return (corredor_Campeao, tempo_menor, volta_menor)