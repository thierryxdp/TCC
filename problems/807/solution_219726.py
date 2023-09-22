def conta_frases (frase):
    excla='!'
    inte='?'
    reti='...'
    final='.'
    if excla in frase:
        return len(excla)
    if inte in frase:
        return len(inte)
    if reti in frase:
        return len(reti)
    if final in frase:
        return len(final)