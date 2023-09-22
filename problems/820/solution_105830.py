def posLetra(frase,letra,numero):
    i=0
    resultado=[]
    j=0
    lista=list(frase)
    while i<len(frase):
        if lista[i]==letra:
            while j<=numero:
                if j==numero:
                    list.append(resultado,i)
                j=j+1
        i=i+1
    return list.index(lista,i)