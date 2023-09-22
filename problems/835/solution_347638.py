def melhor_volta(matriz):
    """ define a mlhor volta entre seis corredores e quem deu essa volta;list->tuple"""  
    i=min([min(matriz[0]),min(matriz[1]),min(matriz[2]),min(matriz[3]),min(matriz[4]),min(matriz[5])])
    resposta2=i
    for volta in matriz:
        if i in volta:
            resposta3= list.index(volta,i)
            
    return (resposta2,resposta3)