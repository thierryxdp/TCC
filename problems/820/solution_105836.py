def posLetra(frase,letra,numero):
    a=0
    b=0
    result=[]
    lista=list(frase)
    while a<len(frase):
        if letra==lista[a]:
            while b<=numero:
                if b==numero:
                    list.append(result, a)
                b=b+1
            
        a=a+1
    if numero>list.count(lista,letra):
        return -1
    return result[0]