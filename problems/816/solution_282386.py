def maiores(frase,n):
    list.append(frase,n)
    list.sort(frase)
    objeto=list.index(frase,n)
    frase=frase[objeto+1:]
    return frase