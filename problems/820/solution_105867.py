def posLetra(frase,letra,numero):
    a=0
    resultado=[]
    b=0
    lista=list(frase)
    while a<len(frase):
        if lista[a]==letra:
            while b<=numero:
                if b==numero:
                    list.append(resultado,a)
                b=b+1
        a=a+1
    if numero>list.count(lista,letra):
        return -1
    return resultado[0]