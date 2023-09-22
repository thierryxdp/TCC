def posLetra(frase,letra,n):
    h=[]
    i=0
    if n<=frase.count(letra):
        while i<len(frase):
            if frase[i] in letra:
            i=i+1
    else:
        return -1