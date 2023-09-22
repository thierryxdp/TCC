def lingua_p(stri):
    ''''''
    trad = ''
    for i in range(len(stri)):
                if stri[i] in 'bcdfghjklmnpqrstvwxyz':
                    trad = trad + stri[i]
                else:
                    trad = trad + stri[i] + 'p' +stri[i]
    return str(trad)