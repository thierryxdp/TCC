def posLetra (string,letra,numero):
    ''''''
    i=0
    ocorrencias = []
    while len(string)>i:
        if str.find(string,letra) == -1:
            return -1
        elif string[i] == letra:
            ocorrencias += [i]
        i+=1
    if len(ocorrencias)<numero:
        return -1
    else: 
        return ocorrencias[numero-1]