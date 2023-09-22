def colchao(a,b,c):
    a = ('A','B','C')
    A = set('A')
    B = set('B')
    C = set('C')
    if(b>A) or (b>B) or (b>C): return True
    elif(b==A) or (b==B) or (b==C): return True
    if(c>A) or (c>B) or (c>C): return True
    elif(c==A) or (c==B) or (c==C): return True
    else: return False