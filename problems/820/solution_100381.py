def posLetra(palavra,letra,numero):
    palavra = [palavra]
    palavraNum = palavra.count(numero)
    if palavraNum >= numero:
        return palavra.find(letra)
    if palavraNum < numero:
        return -1