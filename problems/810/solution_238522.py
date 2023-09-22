def inverte(s):
    s2=s[:-1].replace(',','').replace(';','').lower().split()
    return ' '.join(s2[::-1])