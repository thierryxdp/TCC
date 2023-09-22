def conta_frases (frase):
    excla='!'
    inte='?'
    reti='...'
    final='.'
    if excla in frase:
        return len(excla)
    if inte in frase:
        return len(inte+excla)
    if reti in frase:
        return len(reti+inte+excla)
    if final in frase:
        return len(final+reti+inte+excla)