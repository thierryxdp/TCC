def conta_frases (frase):
    "Dada um texto interido, retorna a quantidade de frases dele, medido pelo número de '.', '?', '!' e '...' . str -> int"
    frase1 = str.replace (frase,'...', '@')
    return frase1.count('.') + frase1.count('!') + frase1.count('?') + frase1.count('@')