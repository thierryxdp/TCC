def posLetra (string,letra,numero):
    ''''''
    inicio = 0 
    ocorrencias = []
    while len(string)>inicio:
        if str.found(string[inicio:],letra) == -1:
            return -1
        else:
            ocorrencias += str.found(string[inicio:],letra)
            inicio = str.found(string[inicio:],letra) + 1
            
    if len(ocorrencias)<numero:
        return -1
    else: 
        return ocorrencias[numero-1]