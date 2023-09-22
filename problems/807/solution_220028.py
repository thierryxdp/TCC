def conta_frases (frase):
    ex=frase.split('!')
    inte=frase.split('?')
    pon=frase.split('.')
    dois=frase.split('...')
    if ex in frase:
        return len(ex)
    if inte in frase:
        return len(inte)
    if pon in frase:
        return len(pon)
    if dois in frase:
        return len(dois)