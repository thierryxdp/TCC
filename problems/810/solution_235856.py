def inverte(frase):
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '...', ' ')
    
    s = str.split(frase)
    
    s = s[::-1]
    
    t = str.join(' ', s)
    
    return t