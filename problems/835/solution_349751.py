def melhor_volta(matriz):
    i = 0 
    j = 0
    resultados = []
    while i < len(matriz):
        mv = min(matriz[j])
        volta = list.index(matriz[j],mv) + 1 
        i = i + 1
        j = j + 1
        list.extend(resultados,[mv, volta])
    return resultados