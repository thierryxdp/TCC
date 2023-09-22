def inverte(frase):
    '''derermina a funcão que returna uma frase de modo inverso'''
    a = str.join(' ', str.split(frase, '.'))
    b = str.join('', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    retorna = e.split(' ')
    retorna2 = retorna[-1:-(len(retorna)+1:-1]
    junta= str.strip(str.join(' ',retorna2))
                            
return str.lower(junta)