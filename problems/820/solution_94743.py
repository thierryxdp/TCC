def posLetra (string,letra,n):
    i=0
    strg=list(string)
    posicao=[]
    if frase.count(letra)<n:
        return -1
    while i<= len(string)-1:
        if frase[i]==letra:
            posicao.append(i)
        i=i+1
    return posicao[(n-1)]