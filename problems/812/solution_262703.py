def retira_pontuacao(f):
    """"""
    if '-' in f:
        return str.replace(f, '-', ' ')
    if ',' in f:
        return str.replace(f, ',', ' ')
    if ':' in f:
        return str.replace(f, ':', ' ')
    if ';' in f:
        return str.replace(f, ';', ' ')
    if '.' in f:
        return str.replace(f, '.', ' ')
    if '!' in f:
        return str.replace(f, '!', ' ')
    if '?' in f:
        return str.replace(f, '?', ' ')