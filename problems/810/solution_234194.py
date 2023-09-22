def inverte(frase):
    '''Recebe uma frase e retorna a mesma na ordem inversa sem letras maiúsculas e sem pontuações.
    string -> string'''

    s = frase
    a = str.replace(s, ',', ' ')
    b = str.replace(a, ':', ' ')
    c = str.replace(b, ';', ' ')
    d = str.replace(c, '.', ' ')
    e = str.replace(d, '...', ' ')
    f = str.replace(e, '!', ' ')
    g = str.replace(f, '?', ' ')
    h = str.replace(g, '-', ' ')
    final = str.replace(h, '    ', ' ')
    
    i = str.lower(final)
    j = str.split(i)
    k = j[::-1]
    
    return str.join(' ',k)