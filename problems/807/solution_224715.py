def conta_frases(frase):
    frase = str.replace(frase,'...', '-')
    return str.split(frase,'-')