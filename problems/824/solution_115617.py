def uppCons(frase):
    ''' Entrada: frase -> dado do tipo string, frese que será
    			 modificada
        
        Saída: A frase com todas as suas consoantes maiusculas
        
        str -> str'''
    i = 0
    frase2 = []
    while i < len(frase):
        if str.lower(frase[i]) in 'bcdfghjklmnpqrstvxywzç':
            frase2.append(str.upper(frase[i]))
        else:
            frase2.append(frase[i])
        i= i+1
    return str.join('',frase2)