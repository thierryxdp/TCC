def lingua_p(string):
    a = string.lower()
    p = 'p'
    vogais = 'aeiouáéíóú'
    for i in vogais:
        string = string.replace(i, i + 'p'+ i)
    return string