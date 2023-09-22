def conta_frases(frases):
    frase_alterada = frases
    frase_alterada = str.replace(frase_alterada,'...','@')
    numero_frases = str.count(frase_alterada,'.')
    numero_frases = str.split(frase_alterada,'@')
    numero_frases = str.split(frase_alterada,'?')
    numero_frases = str.split(frase_alterada,'!')
    return len(lista_frases)