def pontos_por_time(timeA,timeB,pa,pb,timeB,timeA,pB,pA):
    '''H'''
    if pa > pb:
        pontosA = 3
    if pb > pa:
        pontosB = 3
    if pa == pb:
        pontosA and pontosB == 1
    if pB > pA:
        pontosb = 3
    if pA > pB:
        pontosa = 3
    if pA == pB:
        pontosa and pontosb == 1
    pontos_timeA = pontosA + pontosa
    pontos_timeB = pontosB + pontosb
    dicionario = {timeA:pontos_timeA,timeB:pontos_timeB}
    return dicionario