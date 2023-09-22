def conta_frases(s):
    f = s.index('.')
    e = s.index('!')
    i = s.index('?')
    r = s.index('...')
    l1 = [s[:f]]
    l1 = l1 + [s[f+1:e]]
    l1 = l1 + [s[e+1:i]]
    l1 = l1 + [s[i+1:r]]
    return len(l1)