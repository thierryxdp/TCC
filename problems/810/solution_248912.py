def frase(string):
    a = str.replace(string,'!', '')
    b = str.replace(a,'?', '')    
    c = str.replace(b,'...', '[')
    d = str.replace(c,'[', '')
    e = str.replace(d,'-', ' ')
    f = str.replace(e,',', '')
    g = str.replace(f,';', '')      
    h = str.replace(g,':', '')
    i = str.replace(h,'.', '')
    j = str.replace(i, ']', '')
    k = str.replace(j, "'", '')
    return k


def inverte(string):
    a = frase(string)   
    a = str.split(a, ' ')
    list.reverse(a)
    a = str(a)
    a = frase(a)
    a = str.strip(a, ' ')
    a = a.lower()
    return a