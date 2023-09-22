def conta_frases(frase):
    a='!' and '?' and "." and ';' and ':' and '...'
    
    return len(str.split(frase,a))