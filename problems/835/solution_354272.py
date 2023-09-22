def melhor_volta(matriz):
    menor_tempo = 0
    corredor = 0
    for i in range(matriz):
        for j in range(matriz[i]):
			menor_tempo = min(matriz[i])
            corredor = i
    resultado = (corredor,menor_tempo)
    return resultado