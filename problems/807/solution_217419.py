def conta_frases(s):
    if '.' in s:
        f = s.index('.')
    if '!' in s: 
        e = s.index('!')
    if '?' in s:
        i = s.index('?')
    if '...' in s:
    	r = s.index('...')
    l1 = [s[:f]]
    l1 = l1 + [s[f+1:e]]
    l1 = l1 + [s[e+1:i]]
    l1 = l1 + [s[i+1:r]]
    return len(l1)