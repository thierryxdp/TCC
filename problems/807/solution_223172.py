def conta_frases(frases):
    frases.replace('.',' ')
    frases.replace('!',' ')
    frases.replace('?',' ')
    frases.replace('...',' ')
    separar = str.split(frase)
    return len(separar)