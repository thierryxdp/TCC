def conta_frases(string):
    a = str.count(string,'. ')
    b = str.count(string,'...')
    c = str.count(string,'!')
    d = str.count(string,'?')
    return a+b