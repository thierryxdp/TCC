def conta_frases(txt):
    a=txt.replace('!','.')
    b=a.replace('...','.')
    c=b.replace('?','.')
    
    return len(c.split('.'))-1