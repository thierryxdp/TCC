def lingua_p(stri):
    '''funcao que dada a palavra, insere a palavra p antes dela e mantem a vogal em si'''
    trad = ''
    for i in range(len(stri)):
                if stri[i] in 'bcdfghjklmnpqrstvwxyz':
                    trad = trad + stri[i]
                else:
                    trad = trad + stri[i] + 'p' +stri[i]
    return str(trad)