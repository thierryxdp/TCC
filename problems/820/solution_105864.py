def posLetra(frase,letra,numero):
    i=0
    resultado=[]
    j=0
    lista=list(frase)
    while j<=numero:
        if j==numero:
            list.append(resultado,i)
        j=j+1
    i=i+1
    if numero>list.count(lista,letra):
        return -1
    return resultado[0]