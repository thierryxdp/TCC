def invert(frase):
    frase.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ")
    frase_dividida = str.split(" ",sem_ponto)
    inverso = frase_dividida[::-1]
    return inverso