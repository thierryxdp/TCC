def conta_frases(frase):
    return str.count(frase,'!') + str.count(frase,'.') + str.count(frase,'?') + str.count(frase,'...') - 3*str.count(frase,'...')