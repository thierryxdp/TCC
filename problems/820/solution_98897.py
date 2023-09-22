def posLetra(string,letra,ocorrencia):
    a=0
    b=0
    while a<len(string) and b<ocorrencia:
        if string[a]==letra:
            b=b+1
        a=a+1
    if b<ocorrencia:
        return -1
    else:
        return a-1