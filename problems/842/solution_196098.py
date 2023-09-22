def pontos_por_time(jogo):
    ''' retorna o numero total de pontos de cada time
    dada uma lista com dois elementos que são
    dos jogos de ida  e volta (list -> dict)'''
    ida=jogo[0]
    volta=jogo[1]
    nome1=ida[0]
    nome2=ida[1]
    if ida[2][0] > ida[2][1] and volta[2][0] < volta[2][1]:
        pt1 = 6
        pt2 = 0
        return {nome1:pt1, nome2:pt2}
    elif ida[2][0] < ida[2][1] and volta[2][0] > volta[2][1]:
        pt1 = 0
        pt2 = 6
        return {nome1:pt1, nome2:pt2}
    elif ida[2][0] > ida[2][1] and volta[2][0] == volta[2][1]:
        pt1 = 4
        pt2 = 1
        return {nome1:pt1, nome2:pt2}
    elif ida[2][0] < ida[2][1] and volta[2][0] == volta[2][1]:
        pt1 = 1
        pt2 = 4
        return {nome1:pt1, nome2:pt2}
    elif ida[2][0] == ida[2][1] and volta[2][0] < volta[2][1]:
        pt1 = 4
        pt2 = 1
        return {nome1:pt1, nome2:pt2}
    elif ida[2][0] == ida[2][1] and volta[2][0] >volta[2][1]:  
        pt1 = 1
        pt2 = 4        
        return {nome1:pt1, nome2:pt2}
    elif ida[2][0] > ida[2][1] and volta[2][0] > volta[2][1]:
        pt1 = 3
        pt2 = 3
        return {nome1:pt1, nome2:pt2}
    elif ida[2][0] < ida[2][1] and volta[2][0] < volta[2][1]:
        pt1 = 3
        pt2 = 3
        return {nome1:pt1, nome2:pt2}
    else:
        pt1 = 2
        pt2 = 2
        return {nome1:pt1, nome2:pt2}