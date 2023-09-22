def posLetra(string,letra,ocorrencia):
    string = list(string)
    ocorrencias = []
    x = 0 
    while x < len(string):
        if string[x] == letra:
            ocorrencias.append(x)
            x += 1
        x += 1
    if ocorrencia <= (len(ocorrencias)):
        ocorrencia = ocorrencia-1
        ocorrencias[ocorrencia]
        return ocorrencias[ocorrencia]
    else:
        return -1