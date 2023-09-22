def soma_h(N):
    contador=0
    resultadoTotal=0
    while contador!=N:
        contador+=1
        if N==0:
            return round(resultadoTotal,2)
        else:
            resultadoTotal+=1/N
            N=N-1
    return round(resultadoTotal,2)