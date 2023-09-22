def posLetra(frase,letra,numero):
    proximo=0
    posicao=-1
    x=str.index(frase,letra)
    while proximo<numero:
        proximo=proximo+1
        posicao=str.index(frase[posicao+1:],letra)
        x=x+posicao
    return posicao+x