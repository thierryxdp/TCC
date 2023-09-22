def conta_frases(frase):
    """função que retorna a quantidade de frases num texto
    str -> int"""
    if '...' in frase:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...') + str.count(frase,'.') - int(3)
    elif '...' + '...' in frase:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...') + str.count(frase,'.') - int(6) 
    else:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'.')