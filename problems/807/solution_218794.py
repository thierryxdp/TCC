def conta_frases (frase):
    if '! ' in frase:
        return str.replace(frase, '! ', ' ')
    if '?? ' in frase:
        return str.replace(frace,'? ',' ')