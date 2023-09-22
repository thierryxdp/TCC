def lingua_p(w):
    w=w.lower()
    vogais='aeiou'
    for c in vogais:
        w=str.replace(w,c,c+'p')
    return w