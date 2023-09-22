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

    frase_dividida = re.split(espaco \.,' ')
    
    frase_invertida = frase_dividida[::-1]
    
    return frase_invertida