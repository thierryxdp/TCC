def melhor_volta(matriz):
    """funcao que recebe como entrada uma matriz 6 × 10 com 
    os tempos em segundos dos 6 corredores em cada uma das 10
    voltas na pista de Kart, e retorna uma tupla informando 
    de quem foi a melhor volta da prova, com qual tempo e em
    que volta;
    list(list) -> tuple(int/float)"""
    
    tempos = []
    for i in range(len(matriz)):
        for e in matriz [i]:
            tempos += [e]
    menor_tempo = min(tempos)
    corredor = tempos.index(menor_tempo)//10
    volta = tempos.index(menor_tempo)%10
    return (corredor+1,menor_tempo,volta+1)