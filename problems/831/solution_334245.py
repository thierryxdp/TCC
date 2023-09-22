def mapeia(ls,f):
    r=[]
    for e in ls:
        r.append(f(e))
    return r



def eh_vogal(l):
    if l in 'aaeiouáéíóúãõ':
        return True
    else:
        return False

    
def plus_p(p):
    if eh_vogal(p) == True:
        return p + 'p' + p
    else:
        return p


def lingua_p(p):
    r = mapeia(p, plus_p)
    return str.join('', r)