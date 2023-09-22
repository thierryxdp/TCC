def posLetra(frase,letra,numero):
    proximo=0
    posicao=-1
    while proximo<=numero:
        proximo=frase.count(letra)-proximo+1
        posicao=str.index(posLetra[posicao+1:],letra)
    return posicao

posLetra('mariana come banana','a',3)