def conta_frases(frase: str) -> int:
    frase = frase + ' '
    qnt_frases = frase.count('. ') + frase.count('! ') + frase.count('? ') + frase.count('...')
    return qnt_frases