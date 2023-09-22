def conta_frases(string):
    a = str.count(string,'...', -3)
    b = str.count(string,'.',0,-3)
    c = str.count(string,'!')
    d = str.count(string,'?')
    return a+b+c+d