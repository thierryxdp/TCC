def freq_palavras(frases):
    x = 0
    y = {}
    while x < len(str.split(frases)):
        if 'a' in str.split(frases):
            y['a'] = 1
        y[str.split(frases)[x]] = str.count((frases) ,str.split(frases)[x])
        x = x+1 
    return y