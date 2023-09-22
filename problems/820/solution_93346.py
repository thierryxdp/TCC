def posLetra(frase,letra,numero):
    i=0
    posicao=0
    x=0
    while i<numero:
        posicao=str.find(frase[posicao:],letra)+1
        x+=posicao
        i+=1
    return x-1