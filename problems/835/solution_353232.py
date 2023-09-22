def melhor_volta(matriz):
    """Função que dada uma matriz com o tempo das voltas dos corredores, retorna qual corredor e qual volta foi a mais rapida"""
    """list--->int"""
    MV1=min(matriz[0])
    MV2=min(matriz[1])
    MV3=min(matriz[2])
    MV4=min(matriz[3])
    MV5=min(matriz[4])
    MV6=min(matriz[5])
    MV=(MV1,MV2,MV3,MV4,MV5,MV6)
    MVTOTAL=min(MV)
    for c in range(7):
        for v in range(11):
            if matriz[c][v]==MVTOTAL:
                resposta=c+1,v+1
  	return resposta