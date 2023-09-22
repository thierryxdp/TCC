def conta_frases(frases):
    frase_alterada = frases
    frase_alterada = str.replace(frase_alterada,'...','@')
    numero_frases = frase_alterada.count('@')
    numero_frases += frase_alterada.count('.')
    numero_frases += frase_alterada.count('?')
    numero_frases += frase_alterada.count('!')
    return numero_frases