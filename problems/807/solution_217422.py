def conta_frases(s):
    f,e,i,r = 0,0,0,0
    l1 = []
    if '.' in s:
        f = s.index('.')
        l1 = [s[:f]]
    if '!' in s: 
        e = s.index('!')
        l1 = l1 + [s[f+1:e]]
    if '?' in s:
        i = s.index('?')
        l1 = l1 + [s[e+1:i]]
    if '...' in s:
    	r = s.index('...')
        l1 = l1 + [s[i+1:r]]
    return l1