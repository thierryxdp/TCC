def invert(frase):
    sem_ponto = frase.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ")
    frase_dividida = str.split(" ",sem_ponto)
    inverso = frase_dividida[::-1]
    return inverso