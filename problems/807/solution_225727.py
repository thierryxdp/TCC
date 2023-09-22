def conta_frases(string):
    a = str.count(string,'...', -3)
    b = str.count(string,'. ') or str.count(string,'.')
    c = str.count(string,'!')
    d = str.count(string,'?')
    return a+b+c+d