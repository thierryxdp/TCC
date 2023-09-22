def conta_frases(frases):
    ''' função que conta o numero de frases de um texto determinados pelas caracteres especiais ('...', '!', '?', '.' - sem repetições das mesmas)
str -> int'''
    a = frases.count("!")
    b = frases.count("?")
    c = frases.count(".")
    d = frases.count("...")
    if d == 1 and c >=4:
        return (c - 2)+ a + b
    elif d > 0 and c == 0:
        return a+b+d
    elif c > 0 and d == 0:
        return a+b+c
    elif c == 3 and d == 1:
        return a+b+d
    elif d > 1 and c >= 6:
        return (c - 4)+ a + b
    else:
        return a+b+c+d