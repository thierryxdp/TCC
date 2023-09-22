def conta_frases(frase):
    qnt_frases = len(str.split(frase,'.'or'...'or'!'or'?'))
    return qnt_frases -1