def colchao(a,b,c):
    a = ('A','B','C')
    if(b>set('A')) or (b>set('B')) or (b>set('C')): return True
    elif(b==set('A')) or (b==set('B')) or (b==set('C')): return True
    if(c>set('A')) or (c>set('B')) or (c>set('C')): return True
    elif(c==set('A')) or (c==set('B')) or (c==set('C')): return True
    else: return False