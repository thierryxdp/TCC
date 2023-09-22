def pontos_por_time (lista_ambos):
    """Recebe uma lista dois elementos, ambos listas com o formato ''[time], [time, [gol para cada time]" duas vezes, uma para o jogo de ida e outra pro
    de volta. Então, a função calcula o total de pontos para cada time"""
    lista1 = lista_ambos[0]
    lista2 = lista_ambos[1]
    
    Gols1 = lista1[2] #AB
    Gols2 = lista2[2] #BA
    
    TeamA = lista1[0]
    TeamB = lista1[1]
    
    PontosA = 0
    PontosB = 0
    
    if Gols1[0]>Gols1[1]:
        PontosA = PontosA + 3
    if Gols2[1]>Gols2[0]:
        PontosA = PontosA + 3
    if Gols1[0]<Gols1[1]:
        PontosB = PontosB + 3
    if Gols2[1]<Gols2[0]:
        PontosB = PontosB + 3
    if Gols1[0]==Gols1[1]:
        PontosA = PontosA + 1
        PontosB = PontosB + 1
    if Gols2[1]==Gols2[0]:
        PontosA = PontosA + 1
        PontosB = PontosB + 1
    return {TeamA:PontosA, TeamB:PontosB}