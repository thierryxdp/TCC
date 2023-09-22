def melhor_volta(matriz):
    """Funcao recebe uma matriz e retorna o valor equivalente ao menor tempo entre os pilotos, e de quem foi esse tempo
    list -> tuple"""
    melhor = []
    for i in range(len(matriz)):
        melhor.append(min(matriz[i]))
    melhor_corredor = melhor.index(min(melhor))+1
    n_volta = (matriz[melhor.index(min(melhor))].index(min(melhor)))+1
    return (melhor_corredor,min(melhor),n_volta)