def pontos_por_time (L2):
    """Recebe uma lista dois elementos, ambos listas com o formato ''[time], [time, [gol para cada time]" duas vezes, uma para o jogo de ida e outra pro
    de volta. Então, a função calcula o total de pontos para cada time"""
    lista1 = L2[0]
    lista2 = L2[1]
    
    Gols1 = lista1[2]
    Gols2 = lista2[2]
    
    TeamA = lista1[0]
    TeamB = lista2[0]
    
    PontosA = 0
    PontosB = 0
    
    if Gols1[0]>Gols1[1] or Gols2[1]>Gols2[0]:
     PontosA = PontosA + 3
    if Gols1[0]<Gols1[1] or Gols2[1]<Gols2[0]:
     PontosB = PontosB + 3
    if Gols1[0]==Gols1[1] or Gols2[1]==Gols2[0]:
     PontosA = PontosA + 1, PontosB = PontosB + 1
    return {lista1[0]:PontosA, lista2[0]:PontosB}