def hashtag(s):
    """Retorna a string dada com uma "#' no meio, no final e no começo
       str->str"""
    numero = int(len(s))
    metade = int(len(s)//2)
    if numero%2 == 0:
        return '#'+ s[0:metade] + '#' + s[metade:] + '#'
    else:
        return '#'+ s[0:(metade)] + '#' + s[metade:] + '#'