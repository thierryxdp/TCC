def uppCons(frase):
    """ Função que, dados uma """
    
    i = 0
    cons=""
    
    while i < len(frase):
     
        if frase[i] in 'bcnmqwrtypsdfghjlçzxv':
            cons = cons+ cons.replace(frase[i],frase[i].upper())
        i=i + 1
    return cons