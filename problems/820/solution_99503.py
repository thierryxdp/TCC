def posLetra (string,letra,numero):
    ''''''
    inicio = 0 
    ocorrencias = []
    while len(string)>inicio:
        if str.found(string,letra [inicio:-1]) == -1:
            return -1
        else:
            ocorrencias += str.found(string,letra [inicio:-1])
            inicio = str.found(string,letra [inicio:-1]) + 1
    if len(ocorrencias)<numero:
        return -1
    else: 
        return ocorrencias[numero-1]