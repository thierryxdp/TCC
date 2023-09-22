def inverte(frase):
    x = str.replace(frase,'.' , ' ')
    y = str.replace(x,',', ' ')
    z = str.replace(y,'!', ' ')
    t = str.replace(z,'-', ' ')
    i = str.replace(t,'?', ' ')  
    m = str.lower(i)
    s = str.split(m)
    k = str.join(' '('s')
    inverte = k[::-1]
    return inverte