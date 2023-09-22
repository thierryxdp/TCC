def conta_frases(frase):
    if str.find(frase,['.','!','?','...']):
        return len(str.split(frase))