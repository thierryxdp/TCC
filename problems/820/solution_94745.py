def posLetra (string,letra,n):
    i=0
    string=list(string)
    posicao=[]
    if string.count(letra)<n:
        return -1
    while i<= len(string)-1:
        if string[i]==letra:
            posicao.append(i)
        i=i+1
    return posicao[(n-1)]