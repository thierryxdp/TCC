def inverte(frase):
    
    pri = str.join(' ', str.split(frase, '.'))
    sec = str.join('', str.split(pri, ','))
    ter = str.join(' ', str.split(sec, '?'))
    qua = str.join(' ', str.split(ter, '!'))
    qui = str.join(' ', str.split(qua, '-'))
    separar = qui.split(' ')
    oposto = separar[-1:-(len(separar)+1):-1]
    juntos = str.strip(str.join(' ',oposto))
    
    return str.lower(juntos)