def lingua_p(p):
    str.lower(p)
    vogais='aeiou'
    for i in vogais:
        if i in p:
            p=str.join(p,i)
    return p