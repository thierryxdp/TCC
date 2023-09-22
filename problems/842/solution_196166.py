def pontos_por_time(lista):
    '''Função que retorna um dicionario com o nome e o 
    numero de pontos do time na fase
    list -> dict'''
    time1=lista[0][0]
    time2=lista[0][1]
    jogoi=lista[0][2]
    jogov=lista[1][2]
    if jogoi[0]>jogoi[1]:
        p1=3
        p2=0
    if jogoi[0]<jogoi[1]:
        p1=0
        p2=3
    if jogoi[0]==jogoi[1]:
        p1=1
        p2=1
    if jogov[0]>jogov[1]:
        p2=p2+3
    if jogov[0]<jogov[1]:
        p1=p1+3
    if jogov[0]==jogov[1]:
        p1=p1+1
        p2=p2+1
    return {time1:p1,time2:p2}