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
        if x=='i':
            contador = contador + 3
            muda3 = muda2.replace('i', 'ipi')
        if x=='o':
            contador = contador + 4
            muda4 = muda3.replace('o', 'opo')
        if x=='u':
            contador = contador + 5
            muda5 = muda4.replace('u', 'upu')
    return contador