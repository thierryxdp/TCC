def posLetra(frase,letra,n):
    h=[]
    i=0
    if lista.count(letra)==1 and n==2:
        p=list.pop(lista,letra)
        return p+len(lista)
    while i<len(frase):
        if n==1:
            if letra in frase[i]:
                return i
        if n==2:
            list.remove(lista,letra)
            if letra in frase[i]:
                return i
        i=i+1