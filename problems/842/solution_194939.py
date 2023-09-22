def pontos_por_time(lista):
    """função que retorna um dicionario com o nome e pontuação dos times
    lista -> dicionario"""
    t1 = lista[0][0]
    t2 = lista[0][1]
    gol1 = lista[0][2]
    gol2 = lista[1][2]
    if gol1[0]>gol1[1]:
        p1=3
        p2=0
    if gol1[0]<gol1[1]:
        p1=0
        p2=3
    if gol1[0]==gol1[1]:
        p1=1
        p2=1
    if gol2[0]>gol2[1]:
        p2= p2 + 3
    if gol2[0]<gol2[1]:
        p1= p1 + 3
    if gol2[0]==gol2[1]:
        p1= p1 + 1
        p2= p2 + 1
    return {t1:p1,t2:p2}