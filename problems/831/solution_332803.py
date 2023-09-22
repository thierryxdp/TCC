def mapeia(ls,f):
    r=[]
    for e in ls:
        r.append(f(e))
    return r

def lingua_p (word):
    
    ''' str > str
    Recebe uma palavra e retorna essa palavra traduzida para
    a língua do p, ou seja, a cada vogal encontrada na palavra
    é retornada essa vogal + a letra + a mesma vogal'''

    r = mapeia(word, lambda x: x + 'p' + x)
    return str.join('', r)