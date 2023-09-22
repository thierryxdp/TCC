#Start your python function here
def pontos_por_time(lista1):
    ponto11=lista1[0][2][0]
    ponto12=lista1[0][2][1]
    ponto21=lista1[1][2][0]
    ponto22=lista1[1][2][1]
    pontos1=0
    pontos2=0
    
    if ponto11>ponto12:
        pontos1=(pontos1+3)
    if ponto12>ponto11:
        pontos2=(pontos2+3)
    if ponto11==ponto12:
        pontos2=(pontos2+1)
        pontos1=(pontos1+1)
        
    if ponto21<ponto22:
        pontos1=(pontos2+3)
    if ponto22<ponto21:
        pontos2=(pontos2+3)    
    if ponto21==ponto22:
        pontos2=(pontos2+1)
        pontos1=(pontos1+1)
    listadic11=str(lista1[0][0])
    listadic12=str(lista1[0][1])
    dic={listadic12:pontos2,listadic11:pontos1}
    return dic