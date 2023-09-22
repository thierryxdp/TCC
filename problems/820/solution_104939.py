def posLetra(frase,letra,ocorrencia):
    i = 0
    N_ocorrencia= 0
    while i<len(frase) and N_ocorrencia<ocorrencia:
        if frase[i] == letra:
            N_ocorrencia = N_ocorrencia +1
        i = i + 1
    if N_ocorrencia < ocorrencia:
        return -1