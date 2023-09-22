def uppCons(frase):
    """ Função que, dados uma """
    
    i = 0
    
    while i < len(frase):
     
        if frase[i] in 'bcnmqwrtypsdfghjlçzxv':
            frase =frase + frase.replace(frase[i],frase[i].upper())
            i=i + 1
    return frase