#Start your python function here
def pontos_por_time(lista1):
        
    ponto11=lista1[0][2][0]
    ponto12=lista1[0][2][1]
    ponto21=lista1[1][2][0]
    ponto22=lista1[1][2][1]
    pontos1=0
    pontos2=0

    
        

def pontos_por_time(lista1):
        
    ponto11=lista1[0][2][0]
    ponto12=lista1[0][2][1]
    ponto22=lista1[1][2][0]
    ponto21=lista1[1][2][1]
    pontos1=0
    pontos2=0
    if ponto11>ponto12:
            pontos1=(pontos1+3)
    elif ponto12>ponto11:
            pontos2=(pontos2+3)
    elif ponto11==ponto12:
            pontos2=(pontos2+1)
            pontos1=(pontos1+1)
            
    if ponto21>ponto22:
            pontos2=(pontos2+3)
    elif ponto22>ponto21:
            pontos1=(pontos2+3)    
    elif ponto21==ponto22:
            pontos2=(pontos2+1)
            pontos1=(pontos1+1)
    listadic11=str(lista1[0][0])
    listadic12=str(lista1[0][1])
    if str(lista1[0][0])==str(lista1[1][1]):
        dic={listadic12:pontos2,listadic11:pontos1}
        return dic
    if str(lista1[0][1])==str(lista1[1][0]):
        dic={listadic11:pontos2,listadic12:pontos1}
        return dic