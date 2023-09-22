def posLetra(string, letra, n):
    ocorrencias_letra =str.count(string, letra)
    if ocorrencias_letra <n:
        return -1
    i =0
    count =-1
    while i <len(string) and ocorrencias_letra <=n:
        count =count +1
        i =i+1
    return count