def inverte(frase):
    sem_ponto = frase.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ")
    dividida = str.split(" ",sem_ponto)
    inverso = dividida[::-1]
    return inverso