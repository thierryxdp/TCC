def melhor_volta(matriz):
    """ define a mlhor volta entre seis corredores e quem deu essa volta;list->tuple"""
    resposta= matriz
    i=min([min(resposta[0]),min(resposta[1]),min(resposta[2]),min(resposta[3]),min(resposta[4]),min(resposta[5])])
    resposta2=(i)
    for volta in matriz:
        if i in volta:
            resposta2+=volta
    return resposta2