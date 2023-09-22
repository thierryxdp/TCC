def pontos(a,b):
    if a>b:
        return 3
    if a==b:
        return 1
    else: 
        return 0
def pontos_por_time(lista):
    time1=L[0][0]
    time2=L[0][1]
    pontos1=int
    pontos2=int
    if time1==L[1][0]:
        return dict((time1)=(pontos(L[0][2][0],L[0][2][1]))+ (pontos(L[1][2][0],L[1][2][1])),(time2):(pontos(L[0][2][1],L[0][2][0]))+(pontos(L[1][2][1],L[1][2][0])))