def conta_frases(frase):
    string_pontuada=frase.replace('!','.')
    string_pontuada=string_pontuada.replace('?','.')
    string_pontuada=string_pontuada.replace('...','.')
    return string_pontuada.count('.')