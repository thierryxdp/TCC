def posLetra(frase,letra,numero):
     i = 0
    repeticoes = frase.count(letra)
    contador = 0
    if repeticoes<numero :
        return -1
    while i< len(frase):
        if letra in frase:
            contador = contador +1
        if contador == numero:
            posicao = frase.index(letra)
        i = i+1
    return posicao