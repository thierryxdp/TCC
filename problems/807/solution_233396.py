def conta_frases(t):
    t1 = (t)
    if '!' in t:
        t1 = str.replace(t1,'!', '#')
    if '?' in t:
        t1 = str.replace(t1,'?', '#')
    if '.' in t:
        t1 = str.replace(t1, '.', '#')
    if '…' in t:
        t1 = str.replace(t1, '…', '#')
    return len(str.split(t1, '#'))-1