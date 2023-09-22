def posLetra(frase,letra,posicao):
    """calculo e retorno de qual posiçao da fraseaquela letra esta."""
    lista=list(frase)
    i=0
    l=[]
    while i<len(lista):
        if lista[i]==letra:
            l=l+[i]
        i=i+1
    return l[posicao-1]