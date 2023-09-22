def conta_frases(string):
    s=string.replace('?','.')
    s=s.replace('!','.')
    s=s.replace('...','.')
    return len(s.split('.'))-1