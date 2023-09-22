def posLetra(frase,sub,n):
    if n>str.count(frase,sub):
        return -1
    else:
        return frase[str.find(frase,sub)]