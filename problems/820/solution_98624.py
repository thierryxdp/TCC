def posLetra(frase,letra,numero):
    contador=1
    inicio=0
    while contador<= numero:
        posicao = frase.find(letra,inicio)
        inicio = posicao+1
        contador+=1
    return posicao