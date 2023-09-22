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
    if '...' in f:
        sem_ret = str.replace(f, '...', '.')
        return str.replace(sem_ret, '.', ' ')