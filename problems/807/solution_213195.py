def conta_frases(a):
    a=a.replace('...','0')
    a=a.replace('.','0')
    a=a.replace('!','0')
    a=a.replace('?','0')
    return a.count('0')