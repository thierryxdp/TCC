def posLetra(string, letra, n):
    
    i = 0
    ocorrencias = 0
    while i < len(string):
        if string[i] in letra:
            ocorrencias += 1
        i += 1
        if ocorrencias < n:
            return -1
        
    return ocorrencias