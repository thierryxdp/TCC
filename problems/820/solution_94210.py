def posLetra(texto,letra,n):
    ind=1
    p=0
    m=str.index(texto, letra)
    if letra in texto:
        if n==1:
            return m
        elif n > 1:
            return str.find(texto,letra,i+1)
        elif:
            while p < len(texto):
                if texto[p] in letra:
                    ind=ind + 1
                p = p + 1
            return ind