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
    final = str.replace(g, '    ', ' ')
    
    h = str.lower(final)
    i = str.split(h)
    j = i[::-1]
    
    return str.join(' ',j)