def melhor_volta(temposCorredores):
    """ Recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta
    Retorna uma tupla informando: de quem foi a melhor volta da prova, com qual tempo e em
    que volta. Todos os corredores devem possuir tempos diferentes 
    list -> tuple """
    saida = (0,99999999,0)
    i = 0
    for tempos in temposCorredores:
        tempo = min(tempos)
        i += 1
        if tempo<saida[1]:
            saida = (i, tempo, list.index(tempos, tempo)+1)
    return saida