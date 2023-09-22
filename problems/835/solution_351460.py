def melhor_volta(matriz):
    '''Uma pista de Kart permite 10 voltas para cada um dos 6 corredore.
    função receba como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta. A função deve retornar uma tupla informando: 
    De quem foi a melhor volta da prova, com qual tempo e em que volta. Assuma que os corredores tem tempos diferentes.
    list->tuple
teste:melhor_volta([[88, 60, 62, 26, 93, 13, 74, 9, 54, 1], [43, 64, 72, 35, 2, 65, 97, 7, 57, 84], [95, 69, 76, 94, 53, 8, 75, 96, 31, 44],
[36, 98, 16, 71, 59, 99, 19, 30, 46, 100], [18, 58, 49, 89, 37, 14, 82, 66, 51, 77], [85, 87, 17, 50, 67, 90, 63, 47, 22, 101]]) ->(1, 1, 10)'''
    melhor=()
    vencedor_total_volta=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        vencedor_cada_volta=min(matriz[i])
        list.append(vencedor_total_volta,vencedor_cada_volta)
    vencedor=min(vencedor_total_volta)
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]==vencedor:
                corredor=i+1
                volta=j+1
    melhor=melhor+(corredor,vencedor,volta,)
    return melhor