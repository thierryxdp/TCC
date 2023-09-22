def conta_frases(x):
    y = str.replace(x, '-',' ') + str.replace(x, ',',' ') + str.replace(x, ':',' ')
    return y