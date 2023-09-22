def inverte(frase):
    sem_ponto = frase.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ")
    return dividida = str.split(" ",sem_ponto)