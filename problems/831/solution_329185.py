def lingua_p(w):
    w=.lower(w)
    vogais='aeiou'
    for c in vogais:
        w=str.replace(w,c,'p'+c+'p')
    return w