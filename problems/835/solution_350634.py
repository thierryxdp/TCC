def melhor_volta(matriz):
    """Função que retorna uma tupla com (e nessa ordem): quem fez, qual o tempo e em qual volta)"""
    """Parâmetros de entrada:list"""
    """Parâmetros de saída:tup"""
    melhor_Volta=0
    melhor_corredor=0
    melhor_tempo=200000000
    for corredor in range (len(matriz)):
        for volta in range(len(matriz[0])):
            if matriz[corredor][volta]<melhor_tempo:
                melhor_Volta=volta
                melhor_tempo=matriz[corredor][volta]
                melhor_corredor=corredor
    return (melhor_corredor+1,melhor_tempo,melhor_Volta+1)