def conta_frases(frases):
    '''calcula a quantidade de frases em uma sentença, elas estao separadas por . , ! , ... , ?;
    str->int'''
    x=str.count(frases,'...')
    y=str.count(frases,'!')
    z=str.count(frases,'?')
    if x==0:
        w=str.count(frases,'.')
        return w
    else:
        w=str.count(frases,'.')-(3*x)
        return w
    return x+y+z+w