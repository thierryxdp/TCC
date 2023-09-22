def conta_frases(texto):
    subs = str.replace(str.replace(str.replace(texto,"?","."),"!","."),"...",".")
    return len(subs.split("."))-1

# -1 por causa dos pontos no final da frase