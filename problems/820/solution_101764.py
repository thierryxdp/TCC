def posLetra(frase,letra,numero):
    i=0
    num_oco=0
    while len(frase)>i:
        if frase[i]==letra:
            num_oco=num_oco+1
        i=i+1
    if num_oco<numero:
        return -1