def posLetra (string,letra,numero):
    ''''''
    inicio = 0 
    ocorrencias = []
    while len(string)<inicio:
        ocorrencias += str.find (string,letra [inicio:-1])
        inicio += 1
    if len(ocorrencias)-1 < numero:
        return -1
    else:
        return ocorrencias[numero-1]