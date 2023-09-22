def pontos_por_time (elementos):
    '''função que recebe uma list(elementos) que contem informação
    do numero de gols de dois jogos entre dois times e retorna um 
    dict que contem o nome do time e o numero de pontos na fase;
    list->dict'''
    Cormengo=elementos[0][0]
    Flaminthians=elementos[0][1]
    Cormengoi=elementos[0][2][0]
    Cormengov=elementos[1][2][1]
    Flaminthiansi=elementos[0][2][1]
    Flaminthiansv=elementos[1][2][0]
    Cormengop=0
    Flaminthiansp=0
    if Cormengoi>Flaminthiansi:
        Cormengop=3
    if Cormengoi<Flaminthiansi:
        Flaminthiansp=3
    if Cormengoi==Flaminthiansi:
        Cormengop=1
        Flaminthiansp=1
    if Cormengov>Flaminthiansv:
        Cormengop=Cormengop+3
    if Cormengov<Flaminthiansv:
        Flaminthiansp=Flaminthiansp+3
    if  Cormengov==Flaminthiansv:
        Cormengop=Cormengop+1
        Flaminthiansp=Flaminthiansp+1
    return {Cormengo:Cormengop,
            Flaminthians:Flaminthiansp,}