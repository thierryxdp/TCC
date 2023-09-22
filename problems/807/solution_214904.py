def conta_frases(string):
    str.lstrip(string)
    str.rstrip(string)
    return str.count(string, '!')+str.count(string, '?')+str.count(string, '...')+str.count(string, '.')-(str.count(string, '...')*3)