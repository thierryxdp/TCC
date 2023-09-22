def melhor_volta(matriz):
        #receba como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta. A função deve retornar uma tupla informando: De quem foi a melhor volta da prova, com qual tempo e em que volta.
        #entrada : matriz ; saida: vencedor , menor tempo , volta
        #i == voltas
        #t == tempo
    menor_tempo = 1000
    volta = 1000
    vencedor = 1000
    for i in range(0, len(matriz)):
        for o in range(0, len(matriz[i])):
            if min(matriz[i][o], menor_tempo) == matriz[i][o]:
                menor_tempo = min(matriz[i][o], menor_tempo)
                vencedor = i + 1
                volta = o + 1
    return vencedor, menor_tempo, volta