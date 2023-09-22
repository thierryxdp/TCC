def pontos(a,b):
    if a>b:
        return 3
    if a==b:
        return 1
    else: 
        return 0
def pontos_por_time(lista):
    time1=lista[0][0]
    time2=lista[0][1]
    if lista[0][0]==lista[1][0]:
        return dict((lista[0][0])=(pontos(lista[0][2][0],lista[0][2][1]))+(pontos(lista[1][2][0],lista[1][2][1])),(lista[0][1])=(pontos(lista[0][2][1],lista[0][2][0]))+(pontos(lista[1][2][1],lista[1][2][0])))
    if lista[0][0]==lista[1][1]:
        return dict((lista[0][0])=(pontos(lista[0][2][0],lista[0][2][1]))+(pontos(lista[1][2][1],lista[1][2][0])),(lista[0][1])=(pontos(lista[0][2][1],lista[0][2][1]))+(pontos(lista[1][2][1],lista[1][2][0])))