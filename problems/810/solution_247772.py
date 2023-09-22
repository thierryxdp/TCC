def inverte(frase):
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    separar = e.split(' ')
    oposto = separar[-1:-(len(separar)+1):-1]
    juntos = str.strip(str.join(' ',oposto))
    
    return str.lower(juntos)