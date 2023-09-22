def inverte(frase):
    sem_ponto = frase.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ")
    return str.split(" ",sem_ponto)