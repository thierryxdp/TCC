def pontos_por_time(L):
    """função que recebe uma lista de dois elementos e retorna um dicionário cujos mapeamentos são: nome do time -> numero total de pontos na fase. list -> dict"""
    x=0
    y=0
    if L[0][2][0]>L[0][2][1]:
        x=x+3
    if L[0][2][0]<L[0][2][1]:
        y=y+3
    if L[0][2][0]==L[0][2][1]:
        x=x+1
        y=y+1
    if L[1][2][0]>L[1][2][1]:
        y=y+3
    if L[1][2][0]<L[1][2][1]:
        x=x+3
    if L[1][2][0]==L[1][2][1]:
        x=x+1
        y=y+1
    return {L[0][0]:x, L[0][1]:y}