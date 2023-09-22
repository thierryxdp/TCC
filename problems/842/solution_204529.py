def pontos_por_time(L):
    '''recebe uma lista onde cada elemento é tambem uma lista que nos apresenta
    o numero de gols de dois jogos entre dois times e retorna um dicionario com
    o nome de time e o total de pontos na fase'''
    c=0
    f=0
    if L[0][2][0]>L[0][2][1]:
        c=c+3
    if L[0][2][0]<L[0][2][1]:
        f=f+3
    if L[0][2][0]==L[0][2][1]:
        c=c+1
        f=f+1
    if L[1][2][0]>L[1][2][1]:
        f=f+3
    if L[1][2][0]<L[1][2][1]:
        c=c+3
    if L[1][2][0]==L[1][2][1]:
        c=c+1
        f=f+1
    return {L[0][0]:c,L[0][1]:f}