def conta_frases(texto):

    v = str.count(texto,'.')
    x = str.count(texto,'!')
    y = str.count(texto,'?')
    if v>4:
        return (v-2)+x+y
    else:
        return v+x+y