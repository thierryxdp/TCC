def melhor_volta(matriz):
    "recebe uma matriz com os tempos dos corredores em cada volta. Retorna uma tupla com o nome do corredor de melhor volta, o tempo e em qual volta teve esse feito"
    menores = []
    for linha in matriz:
        list.append(menores,min(linha))
    corredor = list.index(menores,min(menores))+1
    tempo = min(menores)
    volta = list.index(matriz[corredor],tempo)+1
    return (corredor,tempo,volta)