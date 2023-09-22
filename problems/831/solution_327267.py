def lingua_p(p):
    contador = 0
    z = p
    novapalavra = ''
    lista = list('palavra')
    vogais = 'a', 'e', 'i', 'o', 'u'
    for x in p:
        if x=='a':
            contador = contador + 1
            muda1 = z.replace('a', 'apa')
        if x=='e':
            contador = contador + 2
            muda2 = muda1.replace('e','epe')
    return muda2