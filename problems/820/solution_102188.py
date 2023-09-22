def posLetra(string,letra,num): 
    i=0
    ocorrencia=0
    while i<len(string):
        if string[i]==letra:
            ocorrencia=ocorrencia+1
        if ocorrencia==num:
            return i
        i=i+1
    return -1