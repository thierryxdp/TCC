def posLetra(frase,letra,numero):
    contador=1
    inicio=0
    while contador<= numero:
        if letra in frase:
        	posicao = frase.index(letra,inicio)
        else:
            posicao = -1
        inicio=posicao+1
        contador+=1
    return posicao