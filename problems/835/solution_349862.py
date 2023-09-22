def melhor_volta(matriz):
    i = 0 
    j = 0
    resultadosmv = []
    resultadosvolta = []
    while i < len(matriz):
        mv = min(matriz[j])
        if mv in matriz[j]:
            copia = matriz[j]
        return copia
        volta = list.index(matriz[j],mv) + 1 
        i = i + 1
        j = j + 1
        list.extend(resultadosmv,[mv])
        list.extend(resultadosvolta,[volta])
    c = min(resultadosmv)
    return (c)