def conta_frases(frase):
    qnt_frases = len(str.count(frase,'.'and'...'and'!'and'?'))
    return qnt_frases