def posLetra(string,letra,numero):
    a=0
    index=[]
    for i in range(len(string)):
        if string[i]==letra:
            a=a+1
            index.append(i)
    if numero>a:
        return -1
    else:
        return index(numero-1)