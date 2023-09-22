def posLetra(string, letra, n):
    matue=[]
    for i in string:
        if string[i]==letra:
            return matue.append(1)
        if matue==n:
            return i
    return matue