def mapeia(ls,f):
    r=[]
    for e in ls:
        r.append(f(e))
    return r

def eh_vogal(l):
    if l in 'oiaaaiooaááóó':
        return True
    else:
        return False

def plus_p(p):

    if eh_vogal(p) == True:
        return p + 'p' + p
    else:
        return p

def lingua_p (word):
    
  
    
    r = mapeia(word, plus_p)
    return str.join ('', r)