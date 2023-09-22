def lingua_p(palavra):
    novapalavra = ''
    a = 'a'
    e = 'e'
    i = 'i'
    o = 'o'
    u = 'u'
    for a in palavra:
        novapalavra = palavra.replace('a',"apa")
    for e in palavra:
        novapalavra = palavra.replace('e',"epe")
    for e in palavra:
        novapalavra = palavra.replace('i',"ipi")
    for e in palavra:
        novapalavra = palavra.replace('o',"o")
    for e in palavra:
        novapalavra = palavra.replace('u',"u")
        return novapalavra