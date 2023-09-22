def melhor_volta(matriz):
    i = 0 
    j = 0
    resultadosmv = []
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
    menor = min(resultadosmv)
    if menor in corredor1:
        corredor = 1
        nvolta = list.index(corredor1,menor) + 1
    if menor in corredor2:
        corredor = 2
        nvolta = list.index(corredor2,menor) + 1
    if menor in corredor3:
        corredor = 3
        nvolta = list.index(corredor3,menor) + 1
    if menor in corredor4:
        corredor = 4
        nvolta = list.index(corredor4,menor) + 1
    if menor in corredor5:
        corredor = 5 
        nvolta = list.index(corredor5,menor) + 1
    if menor in corredor6:
        corredor = 6
        nvolta = list.index(corredor6,menor) + 1   
    return (corredor,menor, nvolta)