def conta_frases (frase):
    excla='!'
    inte='?'
    reti='...'
    final='.'
    if excla in frase:
        return len(frase)
    if inte in frase:
        return len(frase)
    if reti in frase:
        return len(frase)
    if final in frase:
        return len(frase)