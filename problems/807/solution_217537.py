def conta_frases(texto):

    v = str.count(texto,'.')
    x = str.count(texto,'!')
    y = str.count(texto,'?')
    z = str.count(texto,'...')
    if z==1:
        return (v-2)+x+y
    if z==2:
        return (v-4)+x+y
    else:
        return v+x+y