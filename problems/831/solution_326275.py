def lingua_p(p):
    '''retorna uma palavra traduzida na linguagem p;
string -> string'''
    z = len(p)
    for x in range(z):
        if p[x] in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            y = str.replace (p, p[x], p[x] + 'p' + p[x])
    return y