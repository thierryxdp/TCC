def melhor_volta(matriz):
    Minuto=[]
    for linha in matriz:
        tempmin= min(linha)
        list.append(Minuto, tempmin)
        tempo = min(Minuto)
        C= list.index(Minuto,tempo)+1
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if tempo == matriz[linha][coluna]:
                    volta=coluna+1
    return (C,tempo,volta)