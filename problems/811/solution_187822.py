def colchao(a,h,l):
    a = ('A','B','C')
    if (set('A')>=h) or (set('B')>=h) or (set('C')>=h): return False
    if (set('A')>=l) or (set('B')>=l) or (set('C')>=l): return False
    else: return True