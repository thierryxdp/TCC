def conta_frases(s):
    l1 = s.split('.')
    l2 = l1.split('!')
    l3 = l2.split('?')
    l4 = l3.split('...')
    return len(l4)