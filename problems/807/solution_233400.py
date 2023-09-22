def conta_frases(t):
    t1 = (t)
    a = 0
    b = 0
    if str.count(t, '.') >= 3:
        a + 2
    if str.count(t, '.') >= 6:
        b + 4
    if '!' in t:
        t1 = str.replace(t1,'!', '#')
    if '?' in t:
        t1 = str.replace(t1,'?', '#')
    if '.' in t:
        t1 = str.replace(t1, '.', '#')
    if a > 0:
        return len(str.split(t1, '#')) - a
    if b > 3:
        return len(str.split(t1, '#')) - b
    else:
        return len(str.split(t1, '#'))-1