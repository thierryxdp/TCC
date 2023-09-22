def conta_frases(string):
    frases = 0
    string = string.replace('...', '.')
    frases += string.count('!')
    frases += string.count('?')
    frases += string.count('.')
    return frases