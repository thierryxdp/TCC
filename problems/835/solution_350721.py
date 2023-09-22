def melhor_volta(matriz):
    '''recebe como entrada uma matriz 6X10 com os tempos dos corredores em cada volta. A função retorna uma tupla com as seguintes informações: de quem foi a melhor volta, com qual tempo e em que volta; list -> list'''

    corredor = 0
    volta = 0
    aux = min(matriz[0])
    
    for i in range(0,len(matriz)):
        if aux > min(matriz[i]):
            aux = min(matriz[i])
            corredor = i + 1
    for j in range(0,len(matriz[corredor - 1])):
        if aux == matriz[corredor - 1][j]:
            volta = j + 1

    return [corredor, aux, volta]