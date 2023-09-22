def conta_frases(t):
    t1 = (t)
    if '!' in t:
        t1 = str.replace(t1,'!', '#')
    if '?' in t:
        t1 = str.replace(t1,'?', '#')
    if '.' in t:
        t1 = str.replace(t1, '.', '#')
    if str.count(t, '.') >= 6 or str.count(t, '.') >= 3:
        return len(str.split(t1, '#')) - 2
    else:
    	return len(str.split(t1, '#'))-1