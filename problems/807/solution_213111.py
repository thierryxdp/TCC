def conta_frases(s):
    s1 = str.count(s,'...')
    s0 = str.replace(s,'...',' ')
    s2 = str.count(s0,'!')
    s3 = str.count(s0,'?')
    s4 = str.count(s0,'.')
    return s1+s2+s3+s4