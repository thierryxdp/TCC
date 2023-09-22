def pontos_por_time2(placar):
    '''Recebe uma lista contendo duas listas com os times e os
    seus respectivos pontos em duas partida; e retorna um dicionário
    com o nome do time e seus pontos correspondentes
    list, list -> dicionário'''
    Time1 = placar[0][0]
    Time2 = placar[0][1]
    Gols1_part1 = placar[0][2][0]
    Gols2_part1 = placar[0][2][1]
    Gols1_part2 = placar[1][2][1]
    Gols2_part2 = placar[1][2][0]
    
    if int(Gols1_part1) > int(Gols2_part1):
            dicio = {str(Time1): 3, str(Time2): 0}        
    elif int(Gols1_part1) < int(Gols2_part1):
            dicio = {str(Time2): 3, str(Time1): 0}      
    elif int(Gols1_part1) == int(Gols2_part1):
            dicio = {str(Time1): 1, str(Time2): 1}
        
    if int(Gols1_part2) > int(Gols2_part2):
            dicio [str(Time1)] = int(dicio[str(Time1)])+3
    elif int(Gols1_part2) < int(Gols2_part2):
            dicio [str(Time2)] = int(dicio[str(Time2)])+3
    elif int(Gols1_part2) == int(Gols2_part2):
            dicio [str(Time1)] = int(dicio[str(Time1)])+1
            dicio [str(Time2)] = int(dicio[str(Time2)])+1
    
    return dicio