def pontos_por_time(l):
    """list -> list;
    Função que recebe uma lista de dois elementos, onde cada
    elemento é também uma lista que contém o número de gols
    em dois jogos de futebol entre dois times, e retorna um 
    dicionário com o nome dos times e suas pontuações."""
    time1 = l[0][0]
    time2 = l[0][1]
    golst1_j1 = l[0][2][0]
    golst2_j1 = l[0][2][1]
    golst1_j2 = l[1][2][1]
    golst2_j2 = l[1][2][0]
    
    #jogo 1
    ptst1_j1 = 0
    ptst2_j1 = 0
    if golst1_j1 > golst2_j1:
        ptst1_j1 = ptst1_j1 + 3
    if golst1_j1 < golst2_j1:
        ptst2_j1 = ptst2_j1 + 3
    if golst1_j1 == golst2_j1:
        ptst1_j1 = ptst1_j1 + 1
        ptst2_j1 = ptst2_j1 + 1
    #jogo 2
    ptst1_j2 = 0
    ptst2_j2 = 0
    if golst1_j2 > golst2_j2:
        ptst1_j2 = ptst1_j2 + 3
    if golst1_j2 < golst2_j2:
        ptst2_j2 = ptst2_j2 + 3
    if golst1_j2 == golst2_j2:
        ptst1_j2 = ptst1_j2 + 1
        ptst2_j2 = ptst2_j2 + 1
        
    ptst1 = ptst1_j1 + ptst1_j2
    ptst2 = ptst2_j1 + ptst2_j2
    resultado = {time1:ptst1, time2:ptst2}
    return resultado