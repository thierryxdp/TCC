def posLetra(frase,letra,n):
    i=0
    listaletras=[]

    while i < len(frase):
        if frase[i] == letra:
            listaletras+=[str.index(frase[i])]
        i+=1
    return listaletras[n-1]