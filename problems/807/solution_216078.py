def conta_frases(frases):
    ''' função que conta o numero de frases de um texto determinados pelas caracteres especiais ('...', '!', '?', '.' - sem repetições das mesmas)
str -> int'''
    a = frases.count("!")
    b = frases.count("?")
    c = frases.count(".")
    d = frases.count("...")
    if d >= 1 and c >=4:
        return (c - 2)+ a + b
    else:
        return a+b+c+d