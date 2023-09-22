def posLetra(frase,letra,numero):
    i=0
    x=0
    while i<numero:
        posicao=str.find(frase[x+1:],letra)
        x+=posicao
        i+=1
    return x+1