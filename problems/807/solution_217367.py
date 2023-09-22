def conta_frases(s):
    l1 = str(s.split('.'))
    l2 = str(l1.split('!'))
    l3 = str(l2.split('?'))
    l4 = str(l3.split('...'))
    l5 = list(l4)
    return len(l5)