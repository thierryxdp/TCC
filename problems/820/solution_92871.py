def posLetra(string, letra, n):
    ocorrenciasletra =str.count(string, letra)
    if ocorrencias_letra <n:
        return -1
    i =0
    count =-1
    while i <len(string) and ocorrenciasletra <=n:
        count =count +1
        i =i+1
    return count