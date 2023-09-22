def inverte(frase):
    """docs""" 
	
    a = frase
    
	minusculo = str.lower(a)
    
    b = a.replace(',', ' ')
    c = b.replace('.', ' ')
    d = c.replace('!', ' ')
    e = d.replace('-', ' ')
    f = e.replace(':', ' ')
    g = f.replace(';', ' ')
    h = g.replace('?', ' ')
    
    espaco = h

    y = espaco.split()
    
    list1 = list.reverse(y)
    z = ' '.join(y)
    
    return str.lower(z)