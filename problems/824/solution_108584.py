def uppCons(frase):
    
    i = 0
    resp = ''
    
    while i < len(frase):
        if frase[i] in 'AEIOUaeiou':
            resp = resp + str.lower(frase[i])
        if frase[i] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            resp = resp + str.upper(frase[i])
            
        i = i + 1
    
    return resp