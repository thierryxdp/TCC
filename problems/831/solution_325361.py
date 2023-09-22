def lingua_p(pl):
    '''traduz as palavras pra lingua do P. srt->str'''
    pl.lower()
    b=[]
    vogais='aeiou'
    a='a'
    e='e'
    i='i'
    o='o'
    u='u'
    for x in pl:
        if x in vogais:
            if x == a:
                b.append('apa')
            elif x == e:
                b.append('epe')
            elif x == i:
                b.append('ipi')
            elif x == o:
                b.append('opo')
            elif x == u:
                b.append('upu')
        else:
            b.append(x)
    return ''.join(b)