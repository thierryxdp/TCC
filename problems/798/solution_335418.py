def freq_palavras(frases):
    """."""
    y = 0
    b = {}
    p = 0
    a = str.split(frases)
    for x in range(len(a)):
        z = a[y]
        b[z] = p + 1
        y = y + 1    
    return b