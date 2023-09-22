def inverte(frase):
    p = str.replace(frase, '.', ' ')
    p2 = str.replace(p, ',', ' ')
    p3 = str.replace(p2, '?', ' ')
    p4 = str.replace(p3, '!', ' ')
    p5 = str.replace(p4, ';', ' ')
    p6 = str.replace(p5, ':', ' ')
    p7 = str.replace(p6, '-', ' ')
    f1 = str.lower(p7)
    f2 = str.split(f1)
    f3 = f2[ : : -1]
    f4 - str.join(' ', f3)
    return f4