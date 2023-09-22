def posLetra(frase,letra,posiçao):
    """calculo e retorno de qual posiçao da fraseaquela letra esta."""
    lista=list(frase)
    i=0
    k=[]
    while i<len(lista):
        if lista[i]==letra:
            k=k+[i]
        i=i+1
    return k[posiçao-1]