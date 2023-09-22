def mapeia(ls,x):
    r=[]
    
    for e in ls:
        r.append(x(e))
    return r

def eh_vogal(x):
    if x in 'aeiouáéíóúãõ':
        return True
    else:
        return False
    
def p(p):
    if eh_vogal(p) == True:
        return p + 'p' + p
    else:
        return p
    
def lingua_p(frase):
    r = mapeia(frase,p)
    return str.join('',r)