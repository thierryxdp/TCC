def conta_frases(string):
    s=string.replace('?','.')
    s1=s.replace('!','.')
    s2=s1.replace('...','.')
    return len(s2.split('.'))-1