def colchao(a,b,c):
    a = ('A','B','C')
    if(set('A') > b) or (set('B') > b) or (set('C') > b): return False
    elif(set('A')==b) or (set('B')==b) or (set('C')==b): return False
    if(set('A') > c) or (set('B') > c) or (set('C') > c): return False
    elif(set('A')==c) or (set('B')==c) or (set('C')==c): return False
    else: return True