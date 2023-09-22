def pontos_por_time(jogos):
    """A função recebe uma lista de dois elementos onde cada elemento
    é uma lista e retorna um dicionário com o nome de cada time de
    entrada e seu número total de pontos na fase.
    list -> dict"""
    
    pontos = {jogos[0][0]: 0, jogos[0][1]: 0}
    
    if jogos[0][2][0] > jogos[0][2][1]:
        pontos[jogos[0][0]] +=3
        
    elif jogos[0][2][0] == jogos[0][2][1]:
        pontos[jogos[0][0]] += 1
        pontos[jogos[0][1]] += 1
        
    else:
        pontos[jogos[0][1]] += 3
        
        
    if jogos[1][2][0] > jogos[1][2][1]:
        pontos[jogos[1][0]] += 3
        
    elif jogos[1][2][0] == jogos[1][2][1]:
        pontos[jogos[1][0]] += 1
        pontos[jogos[1][1]] += 1
               
    else:
        pontos[jogos[1][1]] +=3
        
    return: pontos