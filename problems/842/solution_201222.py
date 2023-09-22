def pontos_por_time(lista):
    c=0
    f=0
    if(lista[0][2][0] > lista[0][2][1]):
        c=c+3
    if(lista[0][2][0] == lista[0][2][1]):
        c=c+1
        f=f+1
    if(lista[1][2][1] > lista[1][2][0]):
        f=f+3
    if(lista[1][2][1] == lista[1][2][0]):
        c=c+1
        f=f+1

    dict1={
        lista[0][0] : c ,
        lista[0][1] : f
        }
    return dict1