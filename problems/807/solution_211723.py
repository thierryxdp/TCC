def conta_frases(texto):
    '''função que separa um texto contendo frases até final de cada e retorna a quantidade de frases encontradas; str -> int'''
    
    str.split(texto,'.')
    
    if "?" and "!" not in texto and "." in texto: 
        return len(str.split(texto,'.'))-1
    
    if "?" and "!" in texto and "." not in texto:
        return len(str.split(texto,'!'))+len(str.split(texto,'?'))
    
    if "?" and "." in texto and "!" not in texto:
        return len(str.split(texto,'.'))+len(str.split(texto,'?'))
    
    if "." and "!" and "?" in texto:
        return len(str.split(texto,'.'))+len(str.split(texto,'?'))+len(str.split(texto,'!'))-3
    
    if "." and "!" in texto and("?" and "...") not in texto:
        return return len(str.split(texto,'.'))+len(str.split(texto,'!'))