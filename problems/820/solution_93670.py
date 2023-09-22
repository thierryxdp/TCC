def ocorrencia(frase,letra,n):
    
    i = 0
    ocorrencia = 0
    
    
    while ocorrencia <= n:
        if frase[i] <= letra:
            ocorrencia = ocorrencia + 1
            i = i + 1

        else:
            i = i + 1

    return i-1