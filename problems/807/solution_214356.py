def conta_frases(frase):
    """ """
    t = str.replace(str.replace(str.replace(str.replace(frase,'...','/'),'?','/'),'!','/'),'.','/')
    nova = str.split(t,'/')
    quant = len(nova) - 1
    return quant