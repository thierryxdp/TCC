#a função conta o número de frases que aparecem no texto.
#str->int
def conta_frases(frase):
    a=frase.count('.','!','?','...')
    return(a)