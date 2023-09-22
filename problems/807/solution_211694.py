def conta_frases(texto):
    '''função que separa um texto contendo frases até final de cada e retorna a quantidade de frases encontradas; str -> int'''
    
    str.split(texto,'.')
    
    if "?" and "!" not in texto and "." in texto: 
        return len(str.split(texto,'.'))-1
    
    elif "?" and "!" in texto:
        return len(str.split(texto,'!'))+len(str.split(texto,'?'))
    
    elif "?" and "." in texto and :
        return len(str.split(texto,'.'))+len(str.split(texto,'?'))