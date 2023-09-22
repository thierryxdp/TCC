def inverte(frase):
    
    '''
    Nessa usamos o mesma função do problema anterior, para retirar os pontos,
    depois semapramos a frase, mudamos a ordem das palavras e juntamos de novo
    str>str>str
    '''
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    separar = e.split(' ')
    oposto = separar[-1:-(len(separar)+1):-1]
    juntos = str.strip(str.join(' ',oposto))
    
    return str.lower(juntos)