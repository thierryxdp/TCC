def colchao(a,b,c):
    a = ('A','B','C')
    A = set('A')
    B = set('B')
    C = set('C')
    if(b>A): return True
    if(b>B): return True
    if(b>C): return True
    elif(b==A): return True
    elif(b==B): return True
    elif(b==C): return True
    if(c>A) or (c>B) or (c>C): return True
    elif(c==A) or (c==B) or (c==C): return True
    else: return False