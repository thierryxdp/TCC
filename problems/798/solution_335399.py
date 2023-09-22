def freq_palavras(frases):
    """."""
    y = 0
    b = {}
    a = str.split(frases)
    for x in range(len(a)):
        z = a[y]
        b[z] = b[z] + 1
    return b