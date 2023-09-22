def posLetra(string, letra, n):
    ocorrencias_letra =str.count(string, letra)
    if ocorrencias_letra <n:
        return -1
    i =0
    count =0
    while i <len(string) and count <n:
        if string[i] ==letra:
            count =count +1
            
        i =i+1
    return i-1