def conta_frases(frases):
    frase_alterada = frases
    numero_frases = str.replace(frase_alterada,'...','@')
    numero_frases += str.count(frase_alterada,'.')
    numero_frases += str.split(frase_alterada,'@')
    numero_frases += str.split(frase_alterada,'?')
    numero_frases += str.split(frase_alterada,'!')
    return numero_frases