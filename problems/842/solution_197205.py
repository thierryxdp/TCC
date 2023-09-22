def pontos_por_time(L1):
    '''Função que recebe uma lista de dois elementos, onde cada
    cada elemento é também uma lista. A lista completa tem informações
    de jogos de futebol entre dois times. A função retorna um mapeamento
    com o nome do time e o número de pontos na fase.
    list -> dict'''
    C = L1[0][0]
    F = L1[0][1]
    p1 = L1[0][2][0]
    p11 = L1[0][2][1]
    p2 = L1[1][2][0]
    p22 = L1[1][2][1]

    if p1 == p11:
        t = 1 
        d = 1
    if p1 > p11:
        t = 3
        d = 0
    if p1 < p11:
        t = 0
        d = 3
    if p2 == p22:
        r = 1
        q = 1
    if p2 > p22:
        r = 3
        q = 0
    if p2 < p22:
        r = 0
        q = 3

    Map = {C : t + q, F : d + r}
    return Map