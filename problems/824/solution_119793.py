def uppCons(f):
    ''' retorna uma frase com todas as suas consoantes em maiúsculas, dada uma frase f;
    str -> str '''
    i = 0
    x = ''
    while i<len(f):
        if f[i] not in 'a,e,i,o,u,à,á,ã,â,é,ê,í,ô,ó,ú':
            x = x + str.upper(f[i])
        else:
            x = x + f[i]
        i = i + 1
    return x