def melhor_volta(matriz):
    i = 0 
    j = 0
    k = 0
    l = 0
    resultadosmv = []
    resultadosvolta = []
    while i < len(matriz):
        mv = min(matriz[j])
        volta = list.index(matriz[j],mv) + 1 
        i = i + 1
        j = j + 1
        list.extend(resultadosmv,[mv])
        list.extend(resultadosvolta,[volta])
    menor = min(resultadosmv)
    while k < len(matriz):
        if menor in matriz[l]:
            c = list.index(matriz[l],menor)
            return c
    	return (menor,c)