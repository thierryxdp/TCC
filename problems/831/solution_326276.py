def lingua_p(p):
    '''retorna uma palavra traduzida na linguagem p;
string -> string'''
    z = len(p)
    h = ''
    for x in range(z):
        if p[x] in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            h = h + p[x] + 'p' + p[x]
        else:
            h = h + p[x]
    return h