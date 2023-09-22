def posLetra(string,letra,ocorrencia):
    a=0
    b=0
    c=0
    while a<len(string) and b<ocorrencia:
        if string[a]==letra:
            b=b+1
        a=a+1
    return a-1