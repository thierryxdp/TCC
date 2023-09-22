def conta_frases(string):
    str.lstrip(string)
    str.rstrip(string)
    return 1+str.count(string, '!')+str.count(string, '?')+str.count(string, '...')+str.count(string, '.')