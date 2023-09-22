def posLetra(string,letra,ocorrencia):
    string = list(string)
    ocorrencias = []
    i = 0 
    while i < len(string):
        if string[i] == letra:
            ocorrencias.append(i)
            i += 1
        i += 1
    if ocorrencia <= (len(ocorrencias)):
        ocorrencia = ocorrencia-1
        ocorrencias[ocorrencia]
        return ocorrencias[ocorrencia]
    else:
        return -1