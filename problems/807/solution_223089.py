def conta_frases(frase):
    """"""
    if '...' + '...' in frase:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...') + str.count(frase,'.') - int(6)
    elif '...' in frase:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...') + str.count(frase,'.') - int(3)
    else:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'.')