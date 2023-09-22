def soma_h(N):
    contador=0
    resultadoTotal=0
    while contador!=N:
        contador+=1
        resultadoTotal+=1/N
    return round(resultadoTotal,2)