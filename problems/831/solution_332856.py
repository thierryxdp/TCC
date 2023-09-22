def mapeia(ls,f):
    r=[]
    for e in ls:
        r.append(f(e))
    return r

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
    
    ''' str > str
    Recebe uma palavra e retorna essa palavra traduzida para
    a língua do p, ou seja, a cada vogal encontrada na palavra
    é retornada essa vogal + a letra + a mesma vogal'''
    
    r = mapeia(word, plus_p)
    return str.join ('', r)