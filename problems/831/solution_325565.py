def lingua_p(p):
    str.lower(p)
    vogais='aeiou'
    for i in vogais:
        if i in p:
            p=str.split(p,i)
            s=(i+'p').join(p)
    return s