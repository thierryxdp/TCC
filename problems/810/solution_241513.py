def inverte(frase):
    '''Função que inverte a frase dada na variavel frase,
    e retirando dela todas as pontuações e letras maiusculas.
    entrada=string
    saida= string'''
    x = str.replace(frase, ('-'), ' ')
    y = str.replace(x, (','), '')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    b = a.split(' ')
    c = b[-2::-1]
    d =' '.join(c)
    h = d.lower()
    return h