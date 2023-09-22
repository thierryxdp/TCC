def eh_vogal(l):
    if l in 'aeiouáéíóúãõ':
        return True
    else:
        return False

def plus_p(p):

    if eh_vogal(p) == True:
        return p + 'p' + p
    else:
        return p

def lingua_p (word):
    
    r = map(plus_p, word)
    return str.join ('', r)