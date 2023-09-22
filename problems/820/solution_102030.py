def posLetra(string,letra,num):
    i=0
    cont=0
    while i<len(string):
        if string[i]==letra:
            cont+=1
        if cont==num:
            return i
        i+=1
    if cont<num:
        return -1