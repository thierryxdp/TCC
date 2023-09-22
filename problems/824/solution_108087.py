def uppCons(s):
    '''Transforma todas as consoantes da string s em maiúsculas
string -> string'''
    cont = 0
    a = 0
    x = len(s)
    while cont < x:
        y = s[a]
        if y not in 'aeiouAEIOUãÃéíúÉÍÚõÕ':
           s = str.replace(s, s[a], str.upper(s[a]))
        a = a + 1
        cont = cont + 1
    return s