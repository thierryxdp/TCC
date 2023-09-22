def posLetra(frase,letra,numero):
    contador=1
    inicio=0
    while contador<= numero:
        if letra in frase:
        	posicao = frase.index(letra)
        else:
            posicao = -1
        frase=frase[posicao+1:]
        contador+=1
    return posicao