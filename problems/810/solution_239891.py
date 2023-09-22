def inverte(texto):
    ''' função que dado um texto retorna este sem pontua
    ção, letras maiúsculas e com as suas palavras na 
    ordem inversa, dado como entrada o texto. str-> str'''
    a= str.replace(texto, '-', ' ')
    b= str.replace(a, ',', ' ')
    c= str.replace(b, ':', ' ')
    d= str.replace(c, ';', ' ')
    e= str.replace(d, '.', ' ')
    f= str.replace(e, '!', ' ')
    g= str. replace(f, '?', ' ')
    h= str.lower(g)
    i= str.split(h)
    j= i[::-1]
    t_final= str.join(' ', j)
    return t_final