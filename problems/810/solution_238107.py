def inverte (frase):
    
    s = str(frase)
    s = str.replace (s, ',', ' ')
    s = str.replace (s, '.', ' ')
    s = str.replace (s, '!', ' ')
    s = str.replace (s, '?', ' ')
    s = str.replace (s, ':', ' ')
    s = str.replace (s, ';', ' ')
    s = str.replace (s, '-', ' ')
    s = str.lower (s)
    s = str.split (s)
    s = s[::-1]
    
    
    return s