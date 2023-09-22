def posLetra (string,letra,numero):
    ''''''
    inicio = 0 
    ocorrencias = []
    while len(string)<inicio:
        ocorrencias += str.found(string,letra [inicio:-1])
        if ocorrencias == [-1]:
                                 return -1
        else:
                        inicio = str.found(string,letra [inicio:-1]) + 1  
        return ocorrencias[numero-1]