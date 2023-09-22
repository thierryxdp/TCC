def conta_frases(x):
    y = str.replace(x, '...','*')
    return str.count(y, "!") + str.count(y,".") + str.count(y, "?") + str.count(y,"*")