def conta_frases(frase):
    return str.count(frase,'.') + str.count(frase,'aula...') + str.count(frase,'!') + str.count(frase,'?')