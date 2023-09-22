def inverte(frase):
    x = str.replace(frase, '-', ' ')
    y = str.replace(x, ',', ' ')
    z = str.replace(y, ':', ' ')
    a = str.replace(z, ';', ' ')
    b = str.replace(a, '.', ' ')
    c = str.replace(b, '?', ' ')
    d = str.replace(c, '!', ' ')
    k = str.split(d, ' ')
    
    
    
    return k [::-1]