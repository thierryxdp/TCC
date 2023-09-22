def conta_frases(s):
    l1 = str.replace(s,'.','#')
    l2 = str.replace(l1,'!','#')
    l3 = str.replace(l2,'?','#')
    l4 = str.replace(l3,'...','#')
    l5 = l4.split('#',1)
    return len(l5)