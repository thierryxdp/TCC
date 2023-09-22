def melhor_volta(matriz):
    i = 0 
    j = 0
    resultadosmv = []
    resultadosvolta = []
    corredor1 = matriz[0]
    corredor2 = matriz[1]
    corredor3 = matriz[2]
    corredor4 = matriz[3]
    corredor5 = matriz[4]
    corredor6 = matriz[5]
    while i < len(matriz):
        mv = min(matriz[j])
        volta = list.index(matriz[j],mv) + 1 
        i = i + 1
        j = j + 1
        list.extend(resultadosmv,[mv])
        list.extend(resultadosvolta,[volta])
    menor = min(resultadosmv)
    if menor in corredor1:
        nvolta = list.index(corredor1,menor)
    if menor in corredor2:
        nvolta = list.index(corredor2,menor)
    if menor in corredor3:
        nvolta = list.index(corredor3,menor)
    if menor in corredor4:
        nvolta = list.index(corredor4,menor)
    if menor in corredor5:
        nvolta = list.index(corredor5,menor)
    if menor in corredor6:
        nvolta = list.index(corredor6,menor)    
    return (menor, nvolta)