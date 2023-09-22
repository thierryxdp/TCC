def conta_frases(frase): 
    ''' funao que recebe uma strind r retorna um inteiro; str-> int'''
    frase=frase.replace('...','.')
    
    if frase:
        return frase.count('.')  + frase.count('!') +frase.count('?')