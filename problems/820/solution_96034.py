def posLetra(frase, letra, n):

    i = 0
    ocorrencia = 0

    while i <= (len(frase)-1) and ocorrencia <= n - 1:
        if frase[i] == letra:
            ocorrencia = ocorrencia + 1

        i = i + 1
        
    return i - 1