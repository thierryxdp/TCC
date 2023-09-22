def conta_frases(texto):
    """"""
    """"""
    a=str.replace(texto,'!','.')
    b=str.replace(a,'?','.')
    c=str.replace(b,'...','.')
    return len(str.split(c,'.'))-1