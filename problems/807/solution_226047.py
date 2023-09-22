def conta_frases(frases):
    frase_alterada = frases
    lista_frases = str.split(frase_alterada,'...')
    lista_frases = str.split(frase_alterada,'.')
    lista_frases = str.split(frase_alterada,'?')
    lista_frases = str.split(frase_alterada,'!')
    return len(lista_frases)