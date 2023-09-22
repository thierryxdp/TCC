def conta_frases(frase):
    if str.count(frase,'...') > 0:
        return str.count(frase,'!') + str.count(frase,'.') + str.count(frase,'?') + str.count(frase,'...') - 3*str.count(frase,'...')
    else:
        return str.count(frase,'!') + str.count(frase,'.') + str.count(frase,'?') + str.count(frase,'...')