def lingua_p(p):
    z = p
    novapalavra = ''
    lista = list('palavra')
    vogais = 'a', 'e', 'i', 'o', 'u'
    for x in p:
        if x=='a':
            muda1 = z.replace('a', 'apa')
        if x=='e':
            muda2 = muda1.replace('e','epe')
        if x=='i':
            muda3 = muda2.replace('i', 'ipi')
        if x=='o':
            muda4 = muda3.replace('o', 'opo')
        if x=='u':
            muda5 = muda4.replace('u', 'upu')
    return muda5